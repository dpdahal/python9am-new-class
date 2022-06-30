print("============= Computer Bazar =========")
print("1. Dell(Rs:20000) 2. Toshiba(Rs: 30000)  3. Mac(Rs:50000)")
option = int(input("Select any option: "))

dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
gift_box_price = 0
tax_price = 0
if option == 1:
    quantity = int(input("Enter the quantity: "))
    dell_price = 20000 * quantity
elif option == 2:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 30000 * quantity
elif option == 3:
    quantity = int(input("Enter the quantity: "))
    mac_price = 50000 * quantity
else:
    print("Invalid option")
    exit()

total_price = dell_price + toshiba_price + mac_price

print('Delivery 1. Home(Rs:1000) 2. Pickup(Free)')
delivery_option = int(input("Select any option: "))
if delivery_option == 1:
    delivery_price = 1000

print("Packing: 1. Plastic Bab(Rs:500) 2. Bag(Rs:1000) 3. Gift Box(Rs:5000) 4. None")

packing_option = int(input("Select any option: "))
if packing_option == 1:
    plastic_price = 500
elif packing_option == 2:
    bag_price = 1000
elif packing_option == 3:
    gift_box_price = 5000

print("Location: 1. KTM(13% Tax) 2. LTP(FREE) 3.BKT(FREE)")

location_option = int(input("Select any option: "))
if location_option == 1:
    tax_price = total_price * 0.13

grand_total = total_price + delivery_price + plastic_price + bag_price + gift_box_price + tax_price

print(f"Total Quantity: {quantity} \n Total {total_price} \n Tax Amount {tax_price} \n Grand Total {grand_total}")
