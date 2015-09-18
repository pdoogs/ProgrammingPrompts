import sys

digits = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
teens = { 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
tens = { 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90 }
multipliers = { 'hundred':100, 'thousand':1000, 'million':1000000, 'billion': 1000000000 }

def read_tokens():
	tokens = []
	if (len(sys.argv) > 1):
		for i in range(1,len(sys.argv)):
			tokens.append(sys.argv[i])
	else:
		strNum = input('Type a number ("One thousand eighty two") ')
		tokens = strNum.lower().split()
	return tokens

def parse_teens(teenToken, tokens, intVal):
	teenVal = teens[teenToken]
	intVal += teenVal
	tokens = []
	return intVal

def parse_digit(digitToken, tokens, intVal):
	intVal += digits[digitToken]

	if (len(tokens) == 0): return intVal

	tok = tokens.pop(0)
	if (tok in teens):
		intVal *= 100
		intVal = parse_teens(tok, tokens, intVal)
	elif (tok in tens):
		return intVal
	elif (tok in multipliers):
		return intVal
	else:
		return intVal

	return intVal

intVal = 0
tokens = read_tokens()

while len(tokens) > 0:
	tok = tokens.pop(0)
	if (tok == 'zero'):
		intVal = 0
		break
	elif (tok in digits):
		intVal = parse_digit(tok, tokens, intVal)
		break
	elif (tok in teens):
		intVal = parse_teens(tok, tokens, intVal)
		break
		

print(intVal)