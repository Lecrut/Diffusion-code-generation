def render_square_pattern(side_length=7):
    row = '*' * side_length
    pattern = '\n'.join([row] * side_length)
    return pattern

if __name__ == '__main__':
    print(render_square_pattern())