def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    assert add(5, 3) == 8, "Addition test failed"
    assert subtract(10, 4) == 6, "Subtraction test failed"

    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 10 and 4:", subtract(10, 4))