class Animal :
   leg = 'claws'
   def __init__(self) :
      pass
   
class Dog(Animal) :
   def __init__(self , name , age , tail):
      self.name = name
      self.age = age
      self.tail = tail
   def Eating (self , meat) :
       self.meat = meat
         
   
   
class Cat(Animal) :
   def __init__(self ,name , age , tail ):
      self.name = name
      self.age = age
      self.tail = tail
   def get_eat (self , feed) :
         self.feed = feed
      
class Chiken(Animal) :
   def __init__(self  , name ,  age , leg ):
      self.name = name
      self.age = age
      self.leg = leg
   def fight(self , fight ):
      self.fight = fight
   
dog = Dog('Pers' , 2 , 'Хвост')
dog.Eating('Мясо')
cat = Cat('Мурка' , 1 , 'Хвост')
cat.get_eat('Корм')
chiken = Chiken('Мужик' , 3 , 2 )
chiken.fight('Курицой')


print(f'Имя животного :{dog.name} \nВозраст : {dog.age} \nКогти : {dog.leg} \nХвост : {dog.tail} \nкушает : {dog.meat}')
print('---' * 50)
print(f'Имя животного :{cat.name} \nВозраст : {cat.age} \nКогти : {cat.leg} \nХвост : {cat.tail} \n Кушает : {cat.feed}')
print('---' * 50)
print(f'Имя животного :{chiken.name} \nВозраст : {chiken.age} \nКогти : {chiken.leg} \Лапкм : {chiken.leg} \nДерутся : {chiken.fight}')