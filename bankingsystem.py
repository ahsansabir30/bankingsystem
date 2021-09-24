# creating a bnaking system using oop 


from _typeshed import Self

#parent class
class user ():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details (self):
      print("personal details")
      print("")
      print("Name" , Self.name)
    print("Age" , Self.age)
    
    print("Gender" , Self.gender)
 
#child class

class bank (user):
      def __init__(self,name,age,gender):
          super()._init_(name,age,gender)
                
                    self.balance = 0

    
def deposit(self,amount):
                self.balance = self.balance + amount
                print("Account balance has been updated ! : £ " , self.balance )


def withdraw(self,amount):
                self.amount = amount
                if self.amount > self.balance:
                     print("Insufficient Funds | Balance Available: £",self.balance)
                else:
                     self.balance = self.balance-self.amount
                print("Account balance has been updated : £" , self.balance)


                def view_balance(self) :
                    self.show_details()
                    print("Account balance has been updated : £" , self.balance)
