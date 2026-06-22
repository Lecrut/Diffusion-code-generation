def generate_hollow_square(n):
    if n <= 0:
        return
    for i in range(n):
        if i == 0 or i == n - 1:
            yield '#' * n
        else:
            yield '#' + ' ' * (n - 2) + '#'

if __name__ == '__main__':
    n = 5
    for row in generate_hollow_square(n):
        print(row)