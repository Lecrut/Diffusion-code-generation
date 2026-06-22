def generate_number_pyramid():
    size = 6
    return [
        ' ' * (size - i - 1) + ' '.join(str(j) for j in range(1, i + 1))
        for i in range(1, size + 1)
    ]

if __name__ == '__main__':
    result = generate_number_pyramid()
    for line in result:
        print(line)