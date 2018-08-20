def rgb_hex():
  invalid_msg="You typed wrong"
  red=int(input("Enter the Red Value\n:"))
  if red<0 or red>255:
    print(invalid_msg)
  green=int(input("Enter the Green Value:\n"))
  if green<0 or green>255:
    print(invalid_msg)
  blue=int(input("Enter the Blue Value:\n"))
  if blue<0 or blue>255:
    print(invalid_msg)
   
  val=(red<<16)+(green<<8)+blue
  print("{}".format(hex(val)[2:]).upper())
 
def hex_rgb():
  hex_val=input("Enter the Hex value:\n")
  if len(hex_val)!=6:
    print(invalid_msg)
    return
  else:
    hex_val=int(hex_val,16)
  two_hex_digits=2**8
  blue=hex_val % two_hex_digits
  hex_val=hex_val>>8
  green=hex_val%two_hex_digits
  hex_val=hex_val>>8
  red=hex_val % two_hex_digits
  print("Red:{a} Green:{b} Blue: {c}".format(a=red,b=green,c=blue))
  
  
  
def convert():
  while True:
    option=input("Enter 1 to convert RGB to HEX.\nEnter 2 to convert HEX to RGB.\nEnter X to Exit\n")
    if option=='1':
    	print ("RGB to HEX...")
    	rgb_hex()
    elif option=='2':
    	print("HEX to RGB...")
    	hex_rgb()
    elif option=='X':
    	break
    else:
    	print("Error")
convert()
  
  
  
  
    