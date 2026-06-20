def check_value_equality(x, y):
    return x == y

if __name__ == '__main__':
    x1 = 5
    y1 = 5
    print(f"Checking equality between {x1} and {y1}: {check_value_equality(x1, y1)}")
    
    x2 = 10
    y2 = 20
    print(f"Checking equality between {x2} and {y2}: {check_value_equality(x2, y2)}")
    
    x3 = 3.14
    y3 = 3.14
    print(f"Checking equality between {x3} and {y3}: {check_value_equality(x3, y3)}")
    
    x4 = 1.0
    print(f"Checking equality between {x4} and {int(x4)}: {check_value_equality(x4, int(x4))}")