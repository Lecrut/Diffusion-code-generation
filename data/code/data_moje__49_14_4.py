def render_square_pattern(side_length=7):
    line = '*' * side_length
    return '\n'.join([line] * side_length)

if __name__ == '__main__':
    print(render_square_pattern(7))