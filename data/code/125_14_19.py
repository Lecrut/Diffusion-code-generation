def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    NUM1 = 2
    NUM2 = 3
    assert add(NUM1, NUM2) == 5, "Addition test failed"
    assert subtract(NUM2, NUM1) == 1, "Subtraction test failed"
    print("Addition of", NUM1, "and", NUM2, "is:", add(NUM1, NUM2))
    print("Subtraction of", NUM2, "and", NUM1, "is:", subtract(NUM2, NUM1))