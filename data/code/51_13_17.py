import sys

def generate_pyramid(row_count):
    result_lines = []
    for i in range(1, row_count + 1):
        spaces = row_count - i
        half_sequence = list(range(1, i + 1))
        full_sequence = half_sequence + half_sequence[::-1][1:]
        line_parts = [str(num) for num in full_sequence]
        joined_line = ''.join(line_parts)
        formatted_line = ' ' * spaces + joined_line + ' ' * spaces
        result_lines.append(formatted_line)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    hardcoded_rows = 8
    output = generate_pyramid(hardcoded_rows)
    print(output)