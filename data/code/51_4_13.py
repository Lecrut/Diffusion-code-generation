def generate_number_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        current_row = []
        for j in range(1, i + 1):
            current_row.append(str(j))
        result.append(' '.join(current_row))
    return '\n'.join(result)

if __name__ == '__main__':
    rows = 3
    print(generate_number_pyramid(rows))