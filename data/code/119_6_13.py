def reverse_numbers(a, b):
    while a != 0:
        temp = a
        a = b - (b // a) * a
        b = temp
    return b

if __name__ == '__main__':
    x = 15
    y = 25
    result = reverse_numbers(x, y)
    print(f"Reversed numbers: {result}")