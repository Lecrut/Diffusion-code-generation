def generate_hollow_square(side_length, char='X'):
    if side_length < 2:
        return char * side_length
    border_line = char * side_length
    inner_line = char + ' ' * (side_length - 2) + char
    top_bottom = border_line
    middle = '\n'.join([inner_line] * (side_length - 2))
    if side_length == 2:
        return border_line + '\n' + border_line
    return top_bottom + '\n' + middle + '\n' + top_bottom

if __name__ == '__main__':
    print(generate_hollow_square(5, 'X'))