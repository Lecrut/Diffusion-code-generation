def print_diamond(n):
    if n % 2 == 0:
        n = n - 1
    mid = n // 2
    result = []
    for i in range(n):
        spaces = abs(mid - i)
        stars = n - 2 * spaces
        line = ' ' * spaces + '*' * stars
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    size = 8
    print(print_diamond(size))