# Conditional Execution

hrs = input("Enter hours? ")
h = float(hrs)
pay = input("enetr the rate:")
m = float(pay)

if h <= 40:
  print(h * m)
elif h > 40:
  print(40*m + (h-40)*1.5*m)
