class rahi_13:
  def odd(self,a):
    if a%2 !=0:
      return True
    else:
      return False
  def even(self,a):
    if a%2 ==0:
      return True
    else:
      return False
  def prime (self,a):
    for x in range (2,a):
      if (a%x)==0:
        return False
    else:
      return True
  def factorial (self,a):
    factor=1
    for i in range (1,a+1):
      factor=factor*i
    return factor

