def format_multiplication_table(base, width=4, max_multiplier=10):
    lines = []
    for i in range(1, max_multiplier + 1):
        result = base * i
        line = f"{base}{width}x{i}{width}={result}{width}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    base_number = 7
    table_text = format_multiplication_table(base_number)
    print(table_text)