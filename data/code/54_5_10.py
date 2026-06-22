def generate_hollow_square(size=5, char='#', space=' '):
    if size <= 0:
        return ""
    if size == 1:
        return char
    border_line = char * size
    inner_line = char + space * (size - 2) + char
    lines = [border_line]
    inner_rows = [inner_line] * (size - 2)
    combined = (('\n' + inner_line).join([''] * (size - 2))) if size > 2 else ""
    return border_line + combined + (('\n' + border_line) if size > 1 else "")

if __name__ == '__main__':
    print(generate_hollow_square(5))