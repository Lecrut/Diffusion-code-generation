def generate_hollow_square(size, char):
    return '\n'.join([
        char if i in (0, size - 1) or j in (0, size - 1) else ' '
        for i in range(size)
        for j in range(size)
    ])

if __name__ == '__main__':
    result = generate_hollow_square(7, '*')
    print(result)