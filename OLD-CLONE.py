import platform
b = platform.architecture()[0]
if b == '64bit':
  import oldx
elif b == '32bit':
  import oldx
else:print("32bit Not Supported! Sorry")
    

  
    
