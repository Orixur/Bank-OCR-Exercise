
import random

cod = {
	"first" : {
		0 : " _  ",
		1 : "    ",
		2 : " _  ",
		3 : " _  ",
		4 : "    ",
		5 : " _  ",
		6 : " _  ",
		7 : " _  ",
		8 : " _  ",
		9 : " _  ",
	},
	"second" : {
		0 : "| | ",
		1 : "  | ",
		2 : " _| ",
		3 : " _| ",
		4 : "|_| ",
		5 : "|_  ",
		6 : "|_  ",
		7 : "  | ",
		8 : "|_| ",
		9 : "|_| ",
	},
	"third" : {
		0 : "|_| ",
		1 : "  | ",
		2 : "|_  ",
		3 : " _| ",
		4 : "  | ",
		5 : " _| ",
		6 : "|_| ",
		7 : "  | ",
		8 : "|_| ",
		9 : " _| ",
	},
}

def s1(word):
	final = ""
	lastf = 0
	lasts = 1
	lastt = 2
	newLine = False
	for i, letter in enumerate(word):

		if letter == " ":
			firstRow  = "    "
			secondRow = "    "
			thirdRow  = "    "
		elif letter == "\n":
			firstRow  = "\n"
			secondRow = "\n"
			thirdRow  = "\n"
			lastf += 3
			lasts += 3
			lastt += 3
			newLine = True
		else:
			firstRow = cod["first"][int(letter)]
			secondRow = cod["second"][int(letter)]
			thirdRow = cod["third"][int(letter)]

		if final == "":
			final += firstRow + "\n" + secondRow + "\n" + thirdRow
			# print(final)
		elif letter == "\n":
			final += "-" + "\n" + "-" + "\n" + "-"
		else:
			_final = final.split("\n")
			# print(_final)
			_final[lastf] += firstRow + "\n"
			_final[lasts] += secondRow + "\n"
			_final[lastt] += thirdRow + "\n"
			final = "".join(_final)
	return final + "\n"

def s1_new(word):
	final = ""
	firstRow = ""
	secondRow = ""
	thirdRow = ""
	ff = False
	firstRows = []
	secondRows = []
	thirdRows = []
	fftimes = 0
	for i, letter in enumerate(word):
		if letter == " ":
			firstRow  += "    "
			secondRow += "    "
			thirdRow  += "    "
		elif letter == "\n":
			firstRows.append(firstRow)
			secondRows.append(secondRow)
			thirdRows.append(thirdRow)
			firstRow = ""
			secondRow = ""
			thirdRow = ""
			ff = False
			fftimes += 1
		else:
			firstRow += cod["first"][int(letter)]
			secondRow += cod["second"][int(letter)]
			thirdRow += cod["third"][int(letter)]
	firstRows.append(firstRow)
	secondRows.append(secondRow)
	thirdRows.append(thirdRow)
	for cabecera, medio, pie in zip(firstRows, secondRows, thirdRows):
		final += cabecera + "\n"
		final += medio + "\n"
		final += pie + "\n"

	return final
	# print(firstRow)
	# print(secondRow)
	# print(thirdRow)


def fileParser(file):
	_file = file.split("\n")
	print(file)
	decoded = []
	# El ultimo indice no sirve
	if (len(_file)-1) % 3 == 0:
		# Es un archivo valido
		# Con cantidad de vueltas me refiero a la cantidad de filas que hay
		cantidadDeVueltas = (len(_file)-1) / 3
		cont = 0
		row1Number = 0
		row2Number = 1
		row3Number = 2
		while cont < cantidadDeVueltas:
			now = 0
			then = 4
			while then <= len(_file[row1Number]):
				firstRow = _file[row1Number][now:then]
				secondRow = _file[row2Number][now:then]
				thirdRow = _file[row3Number][now:then]
				indexfF = 0
				flag = False
				flag2 = False
				founded = False
				if firstRow == "    " and secondRow == "    " and thirdRow == "    ":
					# Hay un espacio
					decoded.append(" ")
				elif firstRow != "    " or secondRow != "    " or thirdRow != "    ":
					for i, _c in cod["first"].items():
						if firstRow == _c:
							# Encontre una primera fila igual
							foundFirst = _c
							indexfF = i
							flag = True
						if flag:
							if cod["second"][indexfF] == secondRow:
								# Encontre una segunda fila igual
								foundSecond = cod["second"][indexfF]
								flag2 = True
								if flag2:
									if cod["third"][indexfF] == thirdRow:
										# Encontre una tercera fila igual
										founded = True
										decoded.append(str(indexfF))
										break
					if not founded:
						decoded.append("?")
						# # Hay un caracter extraño
						# #
						# # Pense en revisar cada una de las filas actuales y hacer un diccionario de fiting, para ver a cual se asemeja mas, si hay varios con el puntaje mas alto, queda en AMB
						# fitness = {
						# 	"first" : {
						# 		0 : 0,
						# 		1 : 0,
						# 		2 : 0,
						# 		3 : 0,
						# 		4 : 0,
						# 		5 : 0,
						# 		6 : 0,
						# 		7 : 0,
						# 		8 : 0,
						# 		9 : 0,
						# 	},
						# 	"second" : {
						# 		0 : 0,
						# 		1 : 0,
						# 		2 : 0,
						# 		3 : 0,
						# 		4 : 0,
						# 		5 : 0,
						# 		6 : 0,
						# 		7 : 0,
						# 		8 : 0,
						# 		9 : 0,
						# 	},
						# 	"third" : {
						# 		0 : 0,
						# 		1 : 0,
						# 		2 : 0,
						# 		3 : 0,
						# 		4 : 0,
						# 		5 : 0,
						# 		6 : 0,
						# 		7 : 0,
						# 		8 : 0,
						# 		9 : 0,
						# 	},
						# }
						# for i, char1 in enumerate(firstRow):
						# 	for j in range(0, len(list(cod["first"].keys()))):
						# 		if char1 == cod["first"][j][i]:
						# 			# El caracter en la misma posicion es igual
						# 			fitness["first"][j] += 1

						# for i, char1 in enumerate(secondRow):
						# 	for j in range(0, len(list(cod["second"].keys()))):
						# 		if char1 == cod["second"][j][i]:
						# 			# El caracter en la misma posicion es igual
						# 			fitness["second"][j] += 1

						# for i, char1 in enumerate(thirdRow):
						# 	for j in range(0, len(list(cod["third"].keys()))):
						# 		if char1 == cod["third"][j][i]:
						# 			# El caracter en la misma posicion es igual
						# 			fitness["third"][j] += 1
						# # Ahora que tengo los puntajes por posibilidad tengo que ver cual es el que mas se asemeja
						# _fit = {
						# 	0 : 0,
						# 	1 : 0,
						# 	2 : 0,
						# 	3 : 0,
						# 	4 : 0,
						# 	5 : 0,
						# 	6 : 0,
						# 	7 : 0,
						# 	8 : 0,
						# 	9 : 0,
						# }
						# for key, value in fitness.items():
						# 	for key2, value2 in value.items():
						# 		_fit[key2] += value2
						# # Ahora que tengo la suma me fijo el mayor, si hay repetidos significa
						# actualMax = ""
						# nMax = 0
						# enterOne = False
						# for key, value in _fit.items():
						# 	if value > nMax:
						# 		if enterOne:
						# 			decoded.append("!")
						# 			break
						# 		actualMax = str(key)
						# 		nMax = value
						# 		enterOne = True
						# decoded.append(actualMax)

				now = then
				then += 4
			row1Number += 3
			row2Number += 3
			row3Number += 3
			cont += 1
			decoded.append(" ")
	return decoded[:-1]

def s2(word):
	aux = ""
	x = len(word) - 1
	c = 1
	try:
		while c <= len(word):
			aux += word[x]
			x -= 1
			c += 1
		res = [(lambda _l,_i: int(_l)*(_i+1)) (_l, _i) for _i, _l in enumerate(aux)]
		_res = sum(res) % 11
		flag = True if _res == 0 else False
		return flag
		# return (True if (sum([(lambda _l,_i: int(_l)*(_i+1)) (_l, _i) for _i, _l in enumerate(aux)]) % 11) == 0 else False)
	except:
		return "El codigo contiene valores invalidos:" + word

def main():
	# print(s1("302 101 99999999"))
	# print(s2("302"))
	s = fileParser(s1_new("3022193938912382 193190393073821938721931766519832\n123"))
	_s = "".join(s)
	findings = []
	for code in list(_s.split(" ")):
		# print("Codigo: " + code + " || ¿Codigo valido?: " + str(s2(code)))
		if "?" in code:
			findings.append(code + " ILL")
		else:
			findings.append(code + " " + ("ERR" if not s2(code) else "OK" if s2(code) else s2(code)))
	print(findings)

def test():
	# print(s1("123\n123"))
	s1_new("12 3 18391238214712983\n112\n990 900000132913812937481230000\n27091996")

# test()
main()