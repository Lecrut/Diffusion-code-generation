X1 = 5
Y1 = 5
X2 = 10
Y2 = 20
X3 = 3.14
Y3 = 3.14
X4 = 1.0

def check_value_equality(x, y):
    return x == y
if __name__ == '__main__':
    result1 = check_value_equality(X1, Y1)
    print(f'Checking equality between {X1} and {Y1}: {result1}')
    result2 = check_value_equality(X2, Y2)
    print(f'Checking equality between {X2} and {Y2}: {result2}')
    result3 = check_value_equality(X3, Y3)
    print(f'Checking equality between {X3} and {Y3}: {result3}')
    result4 = check_value_equality(X4, X4)
    print(f'Checking equality between {X4} and {X4}: {result4}')