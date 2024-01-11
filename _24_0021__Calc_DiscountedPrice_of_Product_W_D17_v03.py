class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # print(f"An instance was created: {name}")

        #Assert: Runs validations to the received arguments:
        assert price >= 0, f"Price {price} is not greater than zero. Please recheck the number."
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero. Please recheck the number."

        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate   #you MUST specific if you want to access the Class or Attribute level data.

item1 = Item("iPhone", 100, 5)
# item1.name = "iPhone"
# item1.price = 100
# item1.quantity = 5

item2 = Item("Laptop", 1000, 3)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

print(f"The __dict__ for Class Item is: {Item.__dict__}")
print(f"The __dict__ for Instance item1 is: {item1.__dict__}")
print(f"The __dict__ for Instance item2 is: {item2.__dict__}")

item1.apply_discount()   #to process the discount, to ensure it's active, THEN you will print out the price, which is on the mext line:
print(item1.price)
'''
The __dict__ for Class Item is: {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x000002559F52EF70>, 'calculate_total_price': <function Item.calculate_total_price at 0x000002559F550040>, 'apply_discount': <function Item.apply_discount at 0x000002559F5500D0>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
The __dict__ for Instance item1 is: {'name': 'iPhone', 'price': 100, 'quantity': 5}
The __dict__ for Instance item2 is: {'name': 'Laptop', 'price': 1000, 'quantity': 3}
80.0  #here is the applied discount price, kicked in!!!
'''