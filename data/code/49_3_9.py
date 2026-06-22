def generate_star_square(size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row.append('*')
            else:
                row.append(' ')
        result.append(''.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    size = 6
    output = generate_star_square(size)
    print(output)