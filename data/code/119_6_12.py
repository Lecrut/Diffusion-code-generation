def reverse_numbers(a, b):
    while a != 0:
        temp = b - (b // a) * a
        b = a
        a = temp
    return b

if __name__ == '__main__':
    print(reverse_numbers(18, 24))