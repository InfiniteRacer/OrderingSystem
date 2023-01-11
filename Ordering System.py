global cost
global cart
global deliveryfee

cost = 0
cart = {"Start"}
deliveryfee = 10

cart.remove("Start")

def start():

    print("Welcome to the ordering system.")
    print("")

    print("Items:")

    print("- Bread, 10 AED - #100")
    print("- Milk, 15 AED - #101")
    print("- Yogurt, 5 AED - #102")
    print("- Juice, 20 AED - #103")
    print("- Cereal, 15 AED - #104")
    print("- Chicken, 25 AED - #105")
    print("- Fish, 20 AED - #106")
    print("- Eggs, 10 AED - #107")
    print("- Apple, 5 AED - #108")
    print("- Bananna, 10 AED - #109")
    print("- Blueberries, 10 AED - #110")
    print("View cart to delete an item / checkout - #1")
    
    print("")
    enterfirst()
    
def enterfirst():
    
    print("Do NOT enter the #, just the number.")
    print("")
    
    enter()
    
def enter():
    
    global choice
    global cost
    
    choice=input("Enter item number here: ")
    
    if choice == "100":
        print("")
        
        cart.add("Milk")
        cost = cost + 10
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "101":
        print("")
        
        cart.add("Bread")
        cost = cost + 15
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "102":
        print("")
        
        cart.add("Yogurt")
        cost = cost + 5
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "103":
        print("")
        
        cart.add("Juice")
        cost = cost + 20
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "104":
        print("")
        
        cart.add("Cereal")
        cost = cost + 15
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "105":
        print("")
        
        cart.add("Chicken")
        cost = cost + 25
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "106":
        print("")
        
        cart.add("Fish")
        cost = cost + 20
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "107":
        print("")
        
        cart.add("Eggs")
        cost = cost + 10
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "108":
        print("")
        
        cart.add("Apple")
        cost = cost + 5
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "109":
        print("")
        
        cart.add("Bananna")
        cost = cost + 10
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "110":
        print("")
        
        cart.add("Blueberries")
        cost = cost + 10
        
        print("Item added to cart.")
        print("")
        enter()
    elif choice == "1":
        
        print("")
        cartmenu()
        
    else:
        print("")
        print("Invalid input. Please try again.")
        print("Hint: Make sure you havent used the hash (#) and that the number is actually on the list!")
        print("")
        enter()
        
def cartmenu():
    
    print("")
    print("Cart:")
        
    print("")
    print(cart)
    
    print("")
    print("Total: " +str(cost)+ " AED (Not final)")
    
    print("")
    cartmenutwo()
        
def cartmenutwo():
    
    print("Enter '1' to delete an item.")
    print("Press '2' to continue adding items.")
    print("Enter '3' to checkout.")
    
    checkmenufirst=input("Option here: ")
    print("")
    
    if checkmenufirst == "1":

        deleteitems()
        
    elif checkmenufirst == "2":
        
        start()
        
    elif checkmenufirst == "3":
        
        checkoutque()
        
    else:
        print("Invalid input. Please try again! Make sure to just enter the number, nothing else.")
        print("")
        cartmenutwo()
    
def deleteitems():
    
    global cost
    
    print("Enter '1' to cancel and go back to cart menu.")
    itemdelete=input("Enter the item number you entered to add the item (Without the hash): ")
    
    if itemdelete == "100":
        
        cart.remove("Bread")
        cost = cost - 10
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "101":
        
        cart.remove("Milk")
        cost = cost - 15
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "102":
        
        cart.remove("Yogurt")
        cost = cost - 5
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "103":
        
        cart.remove("Juice")
        cost = cost - 20
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "104":
        
        cart.remove("Cereal")
        cost = cost - 15
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "105":
        
        cart.remove("Chicken")
        cost = cost - 25
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "106":
        
        cart.remove("Fish")
        cost = cost - 20
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "107":
        
        cart.remove("Eggs")
        cost = cost - 10
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "108":
        
        cart.remove("Apple")
        cost = cost - 5
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "109":
        
        cart.remove("Bananna")
        cost = cost - 10
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "110":
        
        cart.remove("Blueberries")
        cost = cost - 10
        
        print("Item deleted!")
        
        print("")
        cartmenutwo()
        
    elif itemdelete == "1":
    
        print("")
        cartmenutwo()
        
    else:
        
        print("Invalid input. Please try again! Make sure to enter just the number.")
        print("")
        deleteitems()
        
def checkoutque():
    
    checkpoint=input("Are you sure you want to stop shopping and checkout? (y/n) ")
    
    if checkpoint == 'y':
        
        print("")
        checkoutfinal()
        
    elif checkpoint == 'n':
        
        print("")
        cartmenutwo()
        
    else:
        
        print("")
        print("Invalid input. Try again!")
        print("")
        
        checkoutque()
        
def checkoutfinal():
    
    global vat
    global cost
    global deliveryfee
    
    print("Checkout:")
    print("")
    
    print("Items:")
    print(cart)
    
    print("")
    
    print("Item cost: " +str(cost)+ " AED")
    
    vat = cost * 1.1
    vat = vat - cost
    
    cost = cost + vat
    cost = cost + deliveryfee
    
    vat=round(vat, 2)
    cost=round(cost, 2)
    
    print("Delivery fee: " +str(deliveryfee)+ " AED")
    print("VAT: " +str(vat)+ " AED (10%)")
    
    print("Total: " +str(cost)+ " AED")
    
    exit()
    
start()
