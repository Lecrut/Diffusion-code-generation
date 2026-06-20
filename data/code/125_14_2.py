def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 2) == 3, "Subtraction test failed"
    
    print("Addition of 2 and 3 is:", add(2, 3))
    print("Subtraction of 5 and 2 is:", subtract(5, 2))