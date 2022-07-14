class item:
    pay_rate =0.8 #Class attribute :The pay rate after 20% discount
    def __init__(self, name:str, price:float, quantity=0):
        # typing of each argument is specified and the quantity is initialized to 0 in the constructor
        
        # run validations to the recieved arguments
        
        assert price >=0, f"Price {price} is not grater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not grater than zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = item("phone", 100, 1)
item2 = item("laptop", 1000, 3)

print (item.__dict__) #Prints all attributes in class level
print (item1.__dict__) #Prints all attributes in instance level






 