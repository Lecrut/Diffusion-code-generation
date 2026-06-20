def add_subtract(a, b):
    return a + b, a - b

if __name__ == '__main__':
    result_add, result_sub = add_subtract(5, 3)
    print("Addition:", result_add)
    print("Subtraction:", result_sub)