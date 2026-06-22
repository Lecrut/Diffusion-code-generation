def render_star_square(side_length: int) -> str:
    line = '*' * side_length
    return '\n'.join([line] * side_length)

if __name__ == '__main__':
    side = 7
    print(render_star_square(side))