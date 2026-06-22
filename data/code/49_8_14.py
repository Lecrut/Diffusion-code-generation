def print_star_square():
    config = {
        "size": 9,
        "character": "*"
    }
    side_length = config["size"]
    symbol = config["character"]
    current_row = 0
    output_lines = []
    while current_row < side_length:
        current_col = 0
        current_line_parts = []
        while current_col < side_length:
            current_line_parts.append(symbol)
            current_col += 1
        output_lines.append("".join(current_line_parts))
        current_row += 1
    return "\n".join(output_lines)

if __name__ == '__main__':
    print(print_star_square())