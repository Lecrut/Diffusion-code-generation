def print_diamond():
    lines = []
    n = 7
    for i in range(n):
        if i < (n // 2) + 1:
            spaces = (n // 2) - i
            stars = 2 * i + 1
        else:
            spaces = i - (n // 2)
            stars = 2 * (n - i) - 1
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_diamond())