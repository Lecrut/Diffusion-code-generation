def generate_hollow_square(side_length, char):
    if side_length <= 2:
        return char * side_length
    top_row = char * side_length
    middle_row = char + ' ' * (side_length - 2) + char
    rows = [top_row] + [middle_row] * (side_length - 2) + [top_row]
    return '\n'.join(rows)

if __name__ == '__main__':
    side = 5
    character = 'X'
    print(generate_hollow_square(side, character))