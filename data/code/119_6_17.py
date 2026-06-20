def reverse_numbers(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

if __name__ == '__main__':
    x = 15
    y = 25
    result = reverse_numbers(x, y)
    print(f"Reversed numbers: {result}")