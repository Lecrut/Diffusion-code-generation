def format_multiplication_table():
    max_num = 12
    width = max(len(str(max_num * max_num)) + 1, len(str(max_num)) + 1)
    header = " " * width + "| " + "".join(f"{i:>{width}}" for i in range(1, max_num + 1))
    separator = "-" * len(header)
    lines = [header, separator]
    for i in range(1, max_num + 1):
        row_num = f"{i:>{width}}"
        products = "".join(f"{i * j:>{width}}" for j in range(1, max_num + 1))
        lines.append(f"{row_num} | {products}")
    return "\n".join(lines)

if __name__ == '__main__':
    print(format_multiplication_table())