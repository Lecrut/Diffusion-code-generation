def print_diamond(n):
    half = n // 2
    for i in range(-half, half + 1):
        spaces = abs(i)
        stars = n - 2 * spaces
        line = ' ' * spaces + '*' * stars
        print(line)

if __name__ == '__main__':
    print_diamond(6)