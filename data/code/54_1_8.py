def generate_hollow_square(side_length, character):
    if side_length == 1:
        return character
    top_bottom_row = character * side_length
    middle_row = character + ' ' * (side_length - 2) + character
    rows = [top_bottom_row]
    for _ in range(side_length - 2):
        rows.append(middle_row)
    rows.append(top_bottom_row)
    return '\n'.join(rows)

if __name__ == '__main__':
    side = 5
    char = 'X'
    result = generate_hollow_square(side, char)
    print(result)