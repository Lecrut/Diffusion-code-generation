def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 2) == 3, "Subtraction test failed"
    
    result_add = add(10, 7)
    result_subtract = subtract(10, 7)
    
    print(f"Addition of 10 and 7 is: {result_add}")
    print(f"Subtraction of 10 and 7 is: {result_subtract}")