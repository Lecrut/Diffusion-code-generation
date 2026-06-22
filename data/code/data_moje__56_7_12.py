def generate_multiplication_table(base, rows=10, cols=10, field_width=6):
    table_lines = []
    header = " "*field_width
    for j in range(1, cols + 1):
        header += str(j).rjust(field_width)
    table_lines.append(header)
    for i in range(1, rows + 1):
        line = str(i).rjust(field_width)
        for j in range(1, cols + 1):
            product = base * i * j // base if base != 0 else 0
            product = i * j
            line += str(product).rjust(field_width)
        table_lines.append(line)
    return "\n".join(table_lines)

if __name__ == '__main__':
    result = generate_multiplication_table(5, rows=5, cols=5, field_width=4)
    print(result)