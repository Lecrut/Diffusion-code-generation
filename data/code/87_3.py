def check_value(x):
    return x > 0 and x < 100
if __name__ == '__main__':
    value1 = 50
    value2 = -10
    value3 = 100
    value4 = 101
    print(f"Checking {value1}: {check_value(value1)}")
    print(f"Checking {value2}: {check_value(value2)}")
    print(f"Checking {value3}: {check_value(value3)}")
    print(f"Checking {value4}: {check_value(value4)}")