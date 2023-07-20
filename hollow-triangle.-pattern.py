n=5
for i in range(1,n+1):
  for j in range(i,n+1):
    print(" ",end=" ")
  for j in range(1,i+1):
    if (j==1 or i==n):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for j in range(1,i):
    if (i==j+1 or i==n):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
