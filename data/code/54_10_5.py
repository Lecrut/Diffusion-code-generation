def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    return [
        '*' * size if i == 0 or i == size - 1 else '*' + ' ' * (size - 2) + '*'
        for i in range(size)
    ]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    for line in result:
        print(line)