def generate_number_pyramid(levels: int) -> str:
    result_lines = []
    current_number = 1
    for level in range(1, levels + 1):
        row_numbers = []
        for _ in range(level):
            row_numbers.append(str(current_number))
            current_number += 1
        row_string = " ".join(row_numbers)
        max_width = (levels * 2 - 1) * 2
        result_lines.append(row_string.center(max_width))
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(generate_number_pyramid(4))