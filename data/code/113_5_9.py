MINUS = -1

def subtract_numbers(a, b):
    return a + (b * MINUS)

if __name__ == '__main__':
    result = subtract_numbers(10, 5)
    print(result)