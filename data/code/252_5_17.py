def compare_quantities(quantity1, quantity2):
    if quantity1 == quantity2:
        return "Quantities are equal"
    else:
        return "Quantities are not equal"

if __name__ == '__main__':
    value_a = 45
    value_b = 30
    result = compare_quantities(value_a, value_b)
    print(result)