def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 3) == 2, "Subtraction test failed"
    
    result_add = add(10, 15)
    result_subtract = subtract(20, 8)
    
    print("Addition of 10 and 15:", result_add)
    print("Subtraction of 20 and 8:", result_subtract)