def render_square_stars(side_length: int = 7) -> str:
    return '\n'.join('*' * side_length for _ in range(side_length))

if __name__ == '__main__':
    print(render_square_stars(7))