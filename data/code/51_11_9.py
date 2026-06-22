def build_number_pyramid(height):
    result_lines = []
    for i in range(1, height + 1):
        current_row_numbers = [str(i)] * i
        row_content = " ".join(current_row_numbers)
        spaces_needed = (height - i)
        line = f"{' ' * spaces_needed}{row_content}"
        result_lines.append(line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(build_number_pyramid(7))