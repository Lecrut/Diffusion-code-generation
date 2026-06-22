def format_multiplication_table(base, rows=10, cols=10, width=4):
    header = "   " + " ".join(str(i).rjust(width) for i in range(1, cols + 1))
    lines = [header]
    for i in range(1, rows + 1):
        row_str = str(i).rjust(width)
        for j in range(1, cols + 1):
            product = base * j if i == 1 else i * j
            row_str += str(product).rjust(width)
        lines.append(row_str)
    return "\n".join(lines)

if __name__ == '__main__':
    base = 7
    table = format_multiplication_table(base)
    print(table)