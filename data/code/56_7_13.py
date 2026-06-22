def format_multiplication_table(base, start=1, end=10):
    width = len(str(base * end)) + 2
    lines = []
    for i in range(start, end + 1):
        product = base * i
        line = f"{base:>{width}} x {i:>{width}} = {product:>{width}}"
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(format_multiplication_table(7, 1, 12))