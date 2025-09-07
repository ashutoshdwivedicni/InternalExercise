Operand1=int(input("Enter the Operand-1 Value:"))
Operand2=int(input("Enter the Operand-2 Value:"))
Operator=input("Enter the Operator +,-,*,/:")
if Operator=="+":
  print(Operand1+Operand2)
elif Operator=="-":
  print(Operand1-Operand2)
elif Operator=="*":
  print(Operand1*Operand2)
elif Operator=="/":
  print(Operand1/Operand2)
else:
 print("None")
