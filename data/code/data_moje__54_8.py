def generate_hollow_square(size, char):
    return [
        ''.join(
            char if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' '
            for j in range(size)
        )
        for i in range(size)
    ]

if __name__ == '__main__':
    sample_size = 7
    sample_char = '*'
    result = generate_hollow_square(sample_size, sample_char)
    for line in result:
        print(line)