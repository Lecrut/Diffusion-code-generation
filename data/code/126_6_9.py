X_VALUE = 5
Y_VALUE = 10

def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    result1 = check_equality(X_VALUE, X_VALUE)
    print(f'Checking equality between {X_VALUE} and {X_VALUE}: {result1}')
    result2 = check_equality(Y_VALUE, Y_VALUE)
    print(f'Checking equality between {Y_VALUE} and {Y_VALUE}: {result2}')