def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    x = 15
    y = 7
    result_add = add(x, y)
    result_subtract = subtract(x, y)
    print(f"Addition of {x} and {y}: {result_add}")
    print(f"Subtraction of {y} from {x}: {result_subtract}")