def format_multiplication_table(base, max_factor=10, width=4):
    lines = []
    for factor in range(1, max_factor + 1):
        product = base * factor
        line = f'{factor:<{width}} {base:<{width}} {product:<{width}}'
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    base = 7
    table = format_multiplication_table(base)
    print(table)