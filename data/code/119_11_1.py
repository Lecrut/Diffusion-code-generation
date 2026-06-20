def reverse_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    print(reverse_numbers(5, 10))