def generate_hollow_square(side_length, character):
    if side_length < 1:
        return ""
    if side_length == 1:
        return character
    top_bottom = character * side_length
    middle = character + " " * (side_length - 2) + character
    lines = [top_bottom]
    for _ in range(side_length - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    side = 5
    char = 'X'
    result = generate_hollow_square(side, char)
    print(result)