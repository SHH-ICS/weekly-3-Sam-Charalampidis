print("Info: Large $6.00  Extra Large $10.00\n1 Topping $1.00 2 Toppings $1.75 3 Topping $2.50 4 Topping $3.35")
retry = True
while retry == True:
  pizzas = input("Please chose one for large, or 2 for extra large: ")
  if pizzas == "1":
    pizzas = float(6)
    retry = False
    break
  elif pizzas =="2":
    pizzas = float(10)
    retry = False
    break
  else:
    print("Not an option!")

retry2 = True
while retry2 == True:
  top = input("how many toppings? 1-4 ")
  if top == "1":
    top = float(1)
    retry2 = False
    break
  elif top =="2":
    top = float(1.75)
    retry2 = False
    break
  elif top =="3":
    top = float(2.50)
    retry2 = False
    break
  elif top =="4":
    top = float(3.35)
    retry2 = False
    break
  else:
    print("Not an option!")
subt = pizzas + top
tax = 1.13 * subt - subt
total = subt + tax
print("your subtotal is $"+str(subt))
print("Your tax is " + str(tax))
print("your total is $"+str(round(total)))