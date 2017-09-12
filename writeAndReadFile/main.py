fw = open('sample.txt', 'w')
fw.write('Some text here\n')
fw.write('Python is fun\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()