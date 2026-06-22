def generate_hollow_square(n):
    if n <= 0:
        return []
    return ['*' * n if i == 0 or i == n - 1 else '*' + ' ' * (n - 2) + '*' for i in range(n)]

if __name__ == '__main__':
    print(generate_hollow_square(5))