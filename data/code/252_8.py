def compare_quantities(a, b):
    if a > b:
        print(f"Quantity A is greater than Quantity B")
    elif b > a:
        print(f"Quantity B is greater than Quantity A")
    else:
        print("Quantity A and Quantity B are equal")
if __name__ == '__main__':
    quantity1 = 15
    quantity2 = 25
    compare_quantities(quantity1, quantity2)
    quantity1 = 10
    quantity2 = 10
    compare_quantities(quantity1, quantity2)
    quantity1 = 30
    quantity2 = 5
    compare_quantities(quantity1, quantity2)