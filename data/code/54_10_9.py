def generate_hollow_square(size: int) -> list[str]:
    return [
        ''.join(['*' if (j == 0 or j == size - 1 or i == 0 or i == size - 1) else ' ' for j in range(size)])
        for i in range(size)
    ]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)
    for line in result:
        print(line)