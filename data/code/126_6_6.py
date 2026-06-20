def check_value_equality(x, y):
    return x == y

if __name__ == '__main__':
    value1 = 42
    value2 = 42
    result1 = check_value_equality(value1, value2)
    print(f"Checking equality between {value1} and {value2}: {result1}")
    
    value3 = 7
    value4 = 8
    result2 = check_value_equality(value3, value4)
    print(f"Checking equality between {value3} and {value4}: {result2}")