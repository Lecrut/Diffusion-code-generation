def reverse_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    print(reverse_numbers(x, y))