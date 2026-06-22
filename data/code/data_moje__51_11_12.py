def build_number_pyramid(height: int) -> str:
    max_width = (height * 2 - 1) * 2
    result_lines = []
    for i in range(1, height + 1):
        row_numbers = [str(j) for j in range(1, i + 1)]
        line_content = " ".join(row_numbers)
        padded_line = line_content.center(max_width)
        result_lines.append(padded_line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(build_number_pyramid(7))