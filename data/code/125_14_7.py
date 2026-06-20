def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 3) == 2, "Subtraction test failed"

    print("Addition of 2 and 3 is:", add(2, 3))
    print("Subtraction of 5 from 3 is:", subtract(5, 3))