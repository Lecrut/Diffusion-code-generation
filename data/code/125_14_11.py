def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 3) == 2, "Subtraction test failed"

    result_add = add(10, 15)
    result_subtract = subtract(20, 8)

    print("Addition Result:", result_add)
    print("Subtraction Result:", result_subtract)