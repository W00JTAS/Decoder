import pandas as pd
import re

df = pd.read_csv("challenge-data.csv")
text = input("Please enter your cipher message: ")
wordListText = re.sub("^\W", " ",  text).split()

decryptedList = []
print(wordListText)
for i in range(len(wordListText)):
	print(f'{wordListText[i]} :')
	wordListDF = df[df["cipher"].str.contains(f' {wordListText[i]} ')]
	for row_c, row_d in zip(wordListDF["cipher"], wordListDF['decipher']):
		wordListCipher = re.sub("^\W", " ",  row_c).split()
		wordListDecipher = re.sub("^\W", " ",  row_d).split()
		print(wordListCipher, wordListDecipher)
		for word in wordListCipher:
			if word == wordListText[i]:
				index = wordListCipher.index(word)
				print(index)
				print(wordListDecipher[index])
				decryptedList.append(wordListDecipher[index])
print(f'Your encrypted message: {text}')
print("Your decrypted message:", end=' ')
wordList = [word for i, word in enumerate(decryptedList) if word not in decryptedList[:i]]
for j in wordList:
	print(j, end=' ')
