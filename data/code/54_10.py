def generate_hollow_square(size):
    return [
        ('*' * size if i == 0 or i == size - 1 else ('*' + ' ' * (size - 2) + '*'))
        for i in range(size)
    ]

if __name__ == '__main__':
    print(generate_hollow_square(5))