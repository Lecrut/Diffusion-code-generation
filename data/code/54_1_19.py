def generate_hollow_square(side_length, character):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return character
    line_middle = character + " " * (side_length - 2) + character
    full_line = character * side_length
    lines = [full_line]
    for _ in range(side_length - 2):
        lines.append(line_middle)
    lines.append(full_line)
    return "\n".join(lines)

if __name__ == '__main__':
    side = 5
    char = 'X'
    result = generate_hollow_square(side, char)
    print(result)