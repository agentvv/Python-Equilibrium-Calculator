def equilibrium():
  userIn = input("Please input the chemical equation:\n")
  splitIn = userIn.split("=")
  
  coeff = []
  molecule = []
  concen = []
  k = 1
  
  for i in splitIn[0].split(" "):
    if not i == "+":
      for j in range(len(i)):
        try:
          int(i[j])
        except:
          if j == 0:
            coeff.append(-1)
          else:
            coeff.append("-" + i[:j])
          molecule.append(i[j:])
          break
  
  for i in splitIn[1].split(" "):
    if not i == "+":
      for j in range(len(i)):
        try:
          int(i[j])
        except:
          if j == 0:
            coeff.append(1)
          else:
            coeff.append(i[:j])
          molecule.append(i[j:])
          break
  
  for i in molecule:
    print("The concentration/pressure for", end = " ")
    print(i, end = " ")
    concen.append(float(input("is:")))
  
  for i in range(len(concen)):
    k *= concen[i]**float(coeff[i])
  print("The equilibrium constant is:", k)
