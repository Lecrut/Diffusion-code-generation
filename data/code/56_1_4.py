def generate_multiplication_table(max_number=12):
    max_val = max_number * max_number
    width = len(str(max_val))
    table_lines = []
    header = ''.ljust(width + 2)
    for j in range(1, max_number + 1):
        header += str(j).rjust(width)
    table_lines.append(header)
    separator = '-' * (width + 2 + max_number * width)
    table_lines.append(separator)
    for i in range(1, max_number + 1):
        row = str(i).rjust(width)
        for j in range(1, max_number + 1):
            product = i * j
            row += str(product).rjust(width)
        table_lines.append(row)
    return '\n'.join(table_lines)
if __name__ == '__main__':
    result = generate_multiplication_table(12)
    print(result)