def check_condition(x):
    return x > 0 and x < 100
if __name__ == '__main__':
    value1 = 50
    value2 = 100
    value3 = -10
    value4 = 1000
    print(f"Checking {value1}: {check_condition(value1)}")
    print(f"Checking {value2}: {check_condition(value2)}")
    print(f"Checking {value3}: {check_condition(value3)}")
    print(f"Checking {value4}: {check_condition(value4)}")