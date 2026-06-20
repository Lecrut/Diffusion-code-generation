X = 5
Y = 10

def check_equality(x=X, y=Y):
    return x == y

if __name__ == '__main__':
    result1 = check_equality()
    print(f"Checking equality between {X} and {Y}: {result1}")