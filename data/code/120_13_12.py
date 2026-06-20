def check_equality(val1, val2):
    if val1 == val2:
        return True
    else:
        return False

if __name__ == '__main__':
    value1 = 10
    value2 = 10
    result1 = check_equality(value1, value2)
    print(f"Checking {value1} and {value2}: {result1}")
    
    value3 = "hello"
    value4 = "world"
    result2 = check_equality(value3, value4)
    print(f"Checking {value3} and {value4}: {result2}")
    
    value5 = 3.14
    value6 = 3.140000000000001
    result3 = check_equality(value5, value6)
    print(f"Checking {value5} and {value6}: {result3}")