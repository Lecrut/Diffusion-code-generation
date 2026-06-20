def check_value_equality(x, y):
    return x == y

if __name__ == '__main__':
    result1 = check_value_equality(5, 5)
    print(f"Checking equality between 5 and 5: {result1}")
    result2 = check_value_equality(10, 20)
    print(f"Checking equality between 10 and 20: {result2}")
    result3 = check_value_equality(3.14, 3.14)
    print(f"Checking equality between 3.14 and 3.14: {result3}")
    result4 = check_value_equality(1.0, 1.0)
    print(f"Checking equality between 1.0 and 1.0: {result4}")