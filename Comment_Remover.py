symbol = "#"

file1 = open("english_python_data.txt", "r", encoding="utf8")
file2 = open("Code_2", "w", encoding="utf8")

for line in file1.readlines():

    if line[0] == symbol:
      pass
    elif symbol in line:
      print(line[:line.index(symbol)])
    else:
      print(line)
      file2.write(line)

file2.close()
file1.close()
