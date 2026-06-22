def sort_three_numbers(a, b, c):
    if (a ^ b) < 0:
        a, b = b, a
    if (b ^ c) < 0:
        b, c = c, b
    if (a ^ b) < 0:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    print(sort_three_numbers(3, 1, 2))