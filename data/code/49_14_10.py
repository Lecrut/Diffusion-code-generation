def render_square_pattern(side_length=7):
    return '\n'.join('*' * side_length for _ in range(side_length))

if __name__ == '__main__':
    print(render_square_pattern(7))