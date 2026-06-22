def generate_diamond(n):
    upper = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        upper.append(spaces + stars)
    middle = upper[-1]
    lower = upper[-2][::-1]
    return '\n'.join(upper + [middle] + lower)

if __name__ == '__main__':
    print(generate_diamond(6))