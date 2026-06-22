def generate_hollow_number_pyramid(rows=5):
    result = []
    for i in range(rows):
        row = []
        width = 2 * i + 1
        for j in range(width):
            if i == rows - 1 or j == 0 or j == width - 1:
                row.append(' ' + str(i + 1))
            else:
                row.append('   ')
        result.append(''.join(row).strip())
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_hollow_number_pyramid(5))