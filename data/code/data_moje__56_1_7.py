def generate_multiplication_table(max_num=12):
    max_product = max_num * max_num
    cell_width = len(str(max_product)) + 2
    header = '    '.join((f'{i:>2}' for i in range(1, max_num + 1)))
    lines = [header]
    for i in range(1, max_num + 1):
        row = '    '.join((f'{i * j:>cell_width - 2}' for j in range(1, max_num + 1)))
        lines.append(row)
    return '\n'.join(lines)
if __name__ == '__main__':
    table = generate_multiplication_table(12)
    print(table)