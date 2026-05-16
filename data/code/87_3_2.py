def check_variable(x):
    return x > 0 and x < 100
if __name__ == '__main__':
    value1 = 50
    value2 = 100
    value3 = -10
    value4 = 1000
    print(f"Checking {value1}: {check_variable(value1)}")
    print(f"Checking {value2}: {check_variable(value2)}")
    print(f"Checking {value3}: {check_variable(value3)}")
    print(f"Checking {value4}: {check_variable(value4)}")