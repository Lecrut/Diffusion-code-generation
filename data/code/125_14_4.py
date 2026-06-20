def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 2) == 3, "Subtraction test failed"

    print("Addition result:", add(2, 3))
    print("Subtraction result:", subtract(5, 2))