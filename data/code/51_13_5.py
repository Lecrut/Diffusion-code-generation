def generate_symmetric_number_pyramid(rows):
    results = []
    for i in range(1, rows + 1):
        num_spaces = rows - i
        space_str = ' ' * num_spaces
        line = space_str + str(i) * (2 * i - 1)
        results.append(line)
    return '\n'.join(results)

if __name__ == '__main__':
    print(generate_symmetric_number_pyramid(8))