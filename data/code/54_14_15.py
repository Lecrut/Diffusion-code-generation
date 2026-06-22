def render_hollow_square(side_length, char='*'):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return char
    top_bottom = char * side_length
    middle_row = char + ' ' * (side_length - 2) + char
    return '\n'.join([top_bottom] + [middle_row] * (side_length - 2) + [top_bottom])

if __name__ == '__main__':
    print(render_hollow_square(5, '*'))