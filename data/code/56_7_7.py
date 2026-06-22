def format_multiplication_table(base, width=4):
    result_lines = []
    header = f"{'':>{width}}" + ''.join((f'{i:>{width}}' for i in range(1, 11)))
    result_lines.append(header)
    for row in range(1, 11):
        line = f'{row:>{width}}' + ''.join((f'{base * row:>{width}}' for _ in range(1, 11)))
        result_lines.append(line)
    return '\n'.join(result_lines)
if __name__ == '__main__':
    sample_base = 7
    sample_width = 5
    formatted_table = format_multiplication_table(sample_base, sample_width)
    print(formatted_table)