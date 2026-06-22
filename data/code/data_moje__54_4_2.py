def build_hollow_square(size=10):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    border_line = "*" * size
    middle_line = "*" + " " * (size - 2) + "*"
    top_part = [border_line]
    middle_parts = [middle_line] * (size - 2)
    bottom_part = [border_line]
    all_lines = top_part + middle_parts + bottom_part
    return "\n".join(all_lines)

if __name__ == '__main__':
    size_value = 10
    square_str = build_hollow_square(size_value)
    print(square_str)