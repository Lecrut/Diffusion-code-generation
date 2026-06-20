def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    assert add(5, 3) == 8, "Addition test failed"
    assert subtract(10, 4) == 6, "Subtraction test failed"
    
    print("Addition result:", add(5, 3))
    print("Subtraction result:", subtract(10, 4))