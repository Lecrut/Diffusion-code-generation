def format_multiplication_table(base, width=4):
    table_lines = []
    for i in range(1, 11):
        product = base * i
        line = f"{i} x {base} = {product}".rjust(width * 3 + 5)
        table_lines.append(line)
    return "\n".join(table_lines)

if __name__ == '__main__':
    result = format_multiplication_table(7)
    print(result)