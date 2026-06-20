def check_equality(x, y):
    return x == y

if __name__ == '__main__':
    value1 = 7
    value2 = 7
    result = check_equality(value1, value2)
    print(f"Checking equality between {value1} and {value2}: {result}")

    value3 = 15
    value4 = 30
    result = check_equality(value3, value4)
    print(f"Checking equality between {value3} and {value4}: {result}")