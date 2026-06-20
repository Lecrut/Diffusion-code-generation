def add(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a + b

def subtract(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    print("Addition Result:", result_add)
    print("Subtraction Result:", result_subtract)