def add_decimals(a, b):
    return round(a + b, 2)

if __name__ == '__main__':
    value_one = 4.567
    value_two = 3.14159
    computed_result = add_decimals(value_one, value_two)
    print(computed_result)