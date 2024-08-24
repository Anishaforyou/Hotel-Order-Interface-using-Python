# Define the menu of the restaurant
menu = {
    'chicken egg biryani': 170,
    'chicken biryani with chicken chaap': 240,
    'mutton biryani with chicken chaap': 300,
    'special chicken biryani[2 pieces]': 279,
    'chicken dum biryani': 140,
    'aloo biryani with chicken chaap': 210,
    'aloo biryani': 110,
    'chicken chaap': 100,
    'salad': 50,
}

# Greet
print("Welcome to Biryanis Restaurant")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item.title()}: Rs {price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        print(f"You have ordered {item.title()} for Rs {menu[item]}")
    else:
        print(f"Sorry, the ordered item {item.title()} is not available.")

    another_order = input("Do you want to add another item? (Yes/No): ").lower()  # Convert to lowercase
    if another_order != "yes":
        break

print(f"\nYour total amount to pay is Rs {order_total}")
print(f"Thank You for ordering from us!")
