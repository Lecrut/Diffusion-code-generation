def check_equality(val1, val2):
    if not (isinstance(val1, (int, float, str)) and isinstance(val2, (int, float, str))):
        raise ValueError("Both values must be integers, floats, or strings")
    return val1 == val2

if __name__ == '__main__':
    value1 = 10
    value2 = 10
    print(f"Checking {value1} and {value2}: {check_equality(value1, value2)}")

    value3 = "hello"
    value4 = "world"
    print(f"Checking {value3} and {value4}: {check_equality(value3, value4)}")

    value5 = 3.14
    value6 = 3.140000000000001
    try:
        print(f"Checking {value5} and {value6}: {check_equality(value5, value6)}")
    except ValueError as e:
        print(e)

    value7 = [1, 2, 3]
    value8 = [1, 2, 3]
    print(f"Checking {value7} and {value8}: {check_equality(value7, value8)}")