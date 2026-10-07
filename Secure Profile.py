class UserProfile:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        if self.__age < 1:
            return'Not Set!'
        return self.__age
    @age.setter
    def age(self,newvalue):
        if newvalue > 0:
            self.__age = newvalue
        else:
            print('Error: Age must be positive!')
u = UserProfile('Jimmy',25)
print(u.age)
u.age = -5
print(u.age)
        


