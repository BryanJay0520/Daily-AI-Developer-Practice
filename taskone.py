# # Your tasks:
# 1. Create Python variables to represent the prices and quantities.
# 2. Calculate the total price.
# 3. Print the total.
# 4. Modify your program so it can calculate the total for different quantities.
# Expected result: Your program should calculate the correct total without hardcoding the final answer.

Menu = [
    {"Item": "Miso Ramen", "price": 1160, "quantity": 2},
    {"Item": "Gyoza", "price": 460, "quantity": 1},
    {"Item": "Small Rice", "price": 200, "quantity": 2},
]
total_price = 0
for item in Menu:
    item_total = item["price"] * item["quantity"]
    total_price += item_total
    print(f"{item['Item']} = ¥{item_total}")
print(f"Total Price: ¥{total_price}")