def print_square_stars(side_length: int) -> str:
    return '\n'.join(['*' * side_length for _ in range(side_length)])

if __name__ == '__main__':
    result = print_square_stars(5)
    print(result)