def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 3) == 2, "Subtraction test failed"

    print("Addition result:", add(10, 15))
    print("Subtraction result:", subtract(20, 8))