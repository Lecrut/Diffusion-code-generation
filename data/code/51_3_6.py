def generate_pyramid(n):
    return '\n'.join((''.join((f'{i + 1}' if row == i else ' ' for row in range(2 * n - 1))).center(2 * n - 1) for i in range(n)))
if __name__ == '__main__':
    print(generate_pyramid(7))