def generate_hollow_square(side_length, char):
    if side_length == 1:
        return char
    if side_length == 2:
        return char * 2 + '\n' + char * 2
    lines = []
    first_row = char * side_length
    lines.append(first_row)
    middle_row = char + ' ' * (side_length - 2) + char
    for _ in range(side_length - 2):
        lines.append(middle_row)
    last_row = char * side_length
    lines.append(last_row)
    return '\n'.join(lines)

if __name__ == '__main__':
    side = 5
    symbol = 'X'
    result = generate_hollow_square(side, symbol)
    print(result)