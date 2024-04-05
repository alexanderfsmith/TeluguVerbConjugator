


def telugu_wx_conjugation(root = ['win'], tense = ['nA', 'wunnA', 'wA'], personal = ['nu', 'vu', 'ru', 'xu', 'mu']):
	for i in root:
		for j in tense:
			for k in personal:
				print(i + j + k)



def telugu_wx_conjugation_v2(root = 'hear', tense = 'present', pronoun = 'you', formality = 'casual'):
	telugu = ''
	english = pronoun + ' ' + root
	stem = ''
	match root:
		case 'hear':
			stem = 'tin'
		case 'eat':
			stem = 'win'

	telugu = stem

	match tense:
		case 'past':
			telugu += 'E'
		case 'present':
			telugu += 'wunnA'
		case 'future':
			telugu += 'A'
		case 'negative':
			telugu += 'a'

	match pronoun:
		case 'i':
			telugu += 'nu'
		case 'you':
			match formality:
				case 'casual':
					telugu += 'vu'
				case 'formal':
					telugu += 'ru'
		case 'he':
			match formality:
				case 'casual':
					telugu += 'xu'
				case 'formal':
					telugu += 'ru'
		case 'she':
			match formality:
				case 'casual':
					telugu = stem + 'tunDi'
				case 'formal':
					telugu += 'ru'
		case 'it':
			match formality:
				case 'casual':
					telugu += 'xu'
				case 'formal':
					telugu += 'ru'
		case 'we':
			telugu += 'mu'
		case 'they':
			telugu += 'ru'
		case 'that':
			telugu = stem + 'wundi'
		case 'this':
			telugu = stem + 'wundi'
		case 'those':
			telugu += 'yi'
		case 'these':
			telugu += 'yi'


def telugu_wx_conjugation_v3(telugu = 'tinu', english = ''):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	stem = telugu
	if english == '':
		english = telugu
	
	telugu_word_dict = {}
	count = 0
	#wun/wunna is the durative/continuous suffix w with un meaning to be 
	#E becomes nA or na in front of n
	#andi is the imperative suffix but is not included here/ akandi is the negative imperative suffix
	#dAm is the hortative suffix but is also not included
	#wun is not included because it is technically a compound verb
	for i in ['E', 'wA', 'a']: 
		for j in ['nu', 'vu', 'ru', 'du', 'mu', 'yi']:
			telugu_word_dict[count] = {0:stem, 1:i, 2:j}
			count += 1
			#if the stem ends in a vowel and the suffix starts in a vowel then remove the final vowel in the stem

	telugu_word_dict[count] = {0:stem, 1:'', 2:'wundi'}

	for key_i in telugu_word_dict:
		value_i = telugu_word_dict[key_i]
		tense = ''
		personal = ''
		conjugation = ''
		translation = english
		for key_j in value_i:
			if value_i[key_j] != '':
				for key_k in value_i:
					if key_k > key_j and value_i[key_k] != '':
						match value_i[key_k]:
							case 'E': 
								tense += ' (past)'
							case 'wun':
								tense += ' (durative/continuous)'
							case 'wA':
								tense += ' (future habitual)'
							case 'a':
								tense += ' (future habitual negative)'
							case 'nu':
								personal += ' (first person singular)'
							case 'vu':
								personal += ' (second person singular)'
							case 'ru':
								personal += ' (second person plural and third person masculine plural)'
							case 'du':
								personal += ' (third person masculine singular)'
							case 'mu':
								personal += ' (first person plural)'
							case 'yi':
								personal += ' (third person non-masculine plural)'
							case 'wundi':
								personal += ' (third person non-masculine singular)'

						#krishnamurti page numbers and sections 157 = 15.14 and 265 = 22.6 and 255 = 22.4
						#Rule 1 krishnamurti 265
						if value_i[key_j][-1] in vowels and value_i[key_k][0] in vowels:
							#check for long vowels
							value_i[key_j] = value_i[key_j][:-1]

						#Rule 2a krishnamurti 265
						if value_i[key_j][-1] in ['n'] and len(value_i[key_j]) > 1 and value_i[key_j][-2] in vowels[:5]:
							if value_i[key_k][0] in ['w', 'W']:
								value_i[key_j] = value_i[key_j][:-1] + 'N'
						#Rule 2b krishnamurti 265
						if value_i[key_j][-1] in ['N'] and value_i[key_k][0] in ['w', 'W']:
							#check if retroflex
							value_i[key_k] = 't' + value_i[key_k][1:]
						#Rule 3 krishnamurti 265
						#homorganic stops and affricates
						labial = ['p', 'P', 'b', 'B']
						dental = ['W', 'W', 'x', 'X']
						retroflex = ['t', 'T', 'd', 'D']
						#the palatals and velars have no nasal and are thus not useful to us
						#palatal = ['c', 'C', 'j', 'J']
						#velar = ['k', 'K', 'g', 'G']
						nasal = ['m', 'n', 'N']
						
						if len(value_i[key_j]) > 1 and value_i[key_k][0] not in vowels and value_i[key_j][-1] not in vowels and value_i[key_j][-2] not in vowels and ((value_i[key_j][-2] == 'm' and value_i[key_j][-1] in labial) or (value_i[key_j][-2] == 'n' and value_i[key_j][-1] in dental) or (value_i[key_j][-2] == 'N' and value_i[key_j][-1] in retroflex) ):
							value_i[key_j] = value_i[key_j][:-2] + value_i[key_j][-1]
						
						if len(value_i[key_j]) > 1 and value_i[key_k][0] not in vowels and value_i[key_j][-1] not in vowels and value_i[key_j][-2] not in vowels and value_i[key_j][-1] == value_i[key_j][-2]:
							value_i[key_j] = value_i[key_j][:-2] + value_i[key_j][-1]

						#Rule 4 krishnamurti 265
						if value_i[key_j][-1] in ['c', 'C'] and value_i[key_k][0] in ['w', 'W']:
							value_i[key_j] = value_i[key_j][:-1] + 's'

						#Rule 5a krishnamurti 265
						if value_i[key_j][-1] in ['t', 'T'] and value_i[key_k][0] not in vowels:
							value_i[key_j] = value_i[key_j][:-1] + 'd'

						if value_i[key_j][-1] in ['p'] and value_i[key_k][0] not in vowels:
							value_i[key_j] = value_i[key_j][:-1] + 'b'

						#Rule 5b krishnamurti 265
						stops = ['p', 'P', 't', 'T', 'w', 'W', 'x', 'X', 'd', 'D', 'k', 'K', 'g', 'G']
						if len(value_i[key_j]) > 2 and value_i[key_j][-1] in stops and value_i[key_j][-2] in vowels and value_i[key_j][-3] not in vowels and value_i[key_k][0] not in vowels:
							value_i[key_j] = value_i[key_j] + 'u'

						#Rule 2 157
						if len(value_i[key_j]) > 3 and 'u' in value_i[key_j] and value_i[key_k][0] in ['i', 'I', 'e', 'E']:
							if (value_i[key_j][-1] not in vowels and value_i[key_j][-2] in vowels and value_i[key_j][-3] not in vowels and value_i[key_j][-4] in vowels) or (len(value_i[key_j]) > 4 and value_i[key_j][-1] in vowels and value_i[key_j][-2] not in vowels and value_i[key_j][-3] in vowels and value_i[key_j][-4] not in vowels and value_i[key_j][-5] in vowels):
								u_location = 0
								for count, i in enumerate(reversed(value_i[key_j])):
									if i == 'u':
										u_location = -1 * (count + 1)
										if u_location + 1 == 0:
											value_i[key_j] = value_i[key_j][:u_location] + 'i'
										else:
											value_i[key_j] = value_i[key_j][:u_location] + 'i' + value_i[key_j][u_location + 1:]
										break

						#Rule 6 krishnamurti 265
						#don't really need boundary consonant
						boundary_consonant = False
						u_exists = False
						u_location = 0
						for count, i in enumerate(reversed(value_i[key_j])):
							if i == 'u' and boundary_consonant == False:

								if len(value_i[key_j]) > count + 1 and 'U' in value_i[key_j][-1 * (count+2)]:
									continue
								u_exists = True
								u_location = -1 * (count + 1)
								continue

							if u_exists == True and i not in vowels:
								boundary_consonant = True
								continue

							#if this statement is true there are two syllables
							if u_exists and boundary_consonant and i in vowels:
								#the following morpheme must start with a consonant
								if value_i[key_k][0] not in vowels and len(value_i[key_k]) > 1:
									
									#CCa
									if len(value_i[key_k]) > 2 and value_i[key_k][1] not in vowels and value_i[key_k][2] == 'a':
										if u_location + 1 == 0:
											value_i[key_j] = value_i[key_j][:u_location] + 'a'
										else:
											value_i[key_j] = value_i[key_j][:u_location] + 'a' + value_i[key_j][:u_location]
									#Caa (CA in WX Notation)
									elif value_i[key_k][1] == 'A':
										if u_location + 1 == 0:
											value_i[key_j] = value_i[key_j][:u_location] + 'a'
										else:
											value_i[key_j] = value_i[key_j][:u_location] + 'a' + value_i[key_j][:u_location]
									#Ca
									elif value_i[key_k][1] == 'a':
										if u_location + 1 == 0:
											value_i[key_j] = value_i[key_j][:u_location] + 'a'
										else:
											value_i[key_j] = value_i[key_j][:u_location] + 'a' + value_i[key_j][:u_location]
							
						break
			conjugation += value_i[key_j]
		print(conjugation)
		print(english + tense + personal)
	

	

#roots hear tin eat win
#tenses past present future
#person first second third
#number single multiple
#gender masculine nonmasculine

#suffix		person	number	gender	formality
#nu		first	single  N/A	N/A
#vu		second  single  N/A	casual
#ru		third	N/A	N/A	formal
#du		third	single	masc	casual
#mu
#thundhi
#yi