def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def validate_addition():
    assert add(2, 3) == 5, "Addition test failed"

def validate_subtraction():
    assert subtract(5, 2) == 3, "Subtraction test failed"

if __name__ == '__main__':
    validate_addition()
    validate_subtraction()
    print("Addition of 2 and 3 is:", add(2, 3))
    print("Subtraction of 5 and 2 is:", subtract(5, 2))