from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory=[]
# storing the inventory for the store
# buying a computer (add to inventory)
# selling a computer (remove from inventory)
# updating a computer's price

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}):
        self.inventory= inventory


    # What methods will you need?
    
    def buy(self, computer: Dict[str, Union[str, int, bool]]):

        global itemID
        itemID += 1 # increment itemID
        inventory[itemID] = computer
        return itemID
        
    # 1. call computer(...) constructor 
    #    to create a new computer instance

    # 2. call inventory.append(...) to add the 
    # new computer insatnce to the inventory. 
