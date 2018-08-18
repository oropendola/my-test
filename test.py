

class Test:
  def __init__(self,id,name):
    self.id=id
    self.name=name
  def __str__(self):
    return "Id: {} Name: {}".format(self.id,self.name)
    
t = Test(1,"test")
print(t)
