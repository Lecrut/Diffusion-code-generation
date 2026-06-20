import math

def multiply_numbers(a, b):
    return math.prod([a, b])

if __name__ == '__main__':
    result = multiply_numbers(4, 3)
    print(result)