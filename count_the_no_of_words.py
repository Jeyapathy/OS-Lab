file = open("file_AIDE_30.5.23.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))
