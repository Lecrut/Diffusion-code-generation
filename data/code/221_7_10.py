def sort_three_numbers(a, b, c):
    if (a ^ b) & (b ^ c) >= 0:
        return a, b, c
    elif (a ^ b) & (b ^ c) < 0:
        return a, c, b

if __name__ == '__main__':
    print(sort_three_numbers(5, 1, 3))