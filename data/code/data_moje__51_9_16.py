def build_symmetric_number_pyramid(rows=6):
    max_digit = rows
    max_width = len(str(max_digit ** 2))
    spacing_patterns = []
    for i in range(1, rows + 1):
        current_number = i
        line_parts = []
        for j in range(i):
            num_str = str(current_number)
            padded = num_str.center(max_width + 2)
            line_parts.append(padded)
            current_number += 1
        line = "".join(line_parts).strip()
        total_spaces = max_width * (rows - i) * 2 + 2 * (rows - i)
        left_padding = " " * total_spaces
        spacing_patterns.append(left_padding + line)
    return "\n".join(spacing_patterns)

if __name__ == '__main__':
    result = build_symmetric_number_pyramid(6)
    print(result)