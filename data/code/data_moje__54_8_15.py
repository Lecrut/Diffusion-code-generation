def print_hollow_square(size):
    lines = [
        ''.join(
            '*' if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' '
            for j in range(size)
        )
        for i in range(size)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 7
    result = print_hollow_square(sample_size)
    print(result)