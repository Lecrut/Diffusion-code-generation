def generate_hollow_square(size):
    return [
        ''.join('*' if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' ' for j in range(size))
        for i in range(size)
    ]

if __name__ == '__main__':
    result = generate_hollow_square(7)
    for line in result:
        print(line)