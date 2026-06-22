def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    return ['*' + ' ' * (size - 2) + '*' if i not in (0, size - 1) else '*' * size for i in range(size)]

if __name__ == '__main__':
    print(generate_hollow_square(5))