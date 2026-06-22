def print_square_pattern(side_length: int=5) -> str:
    return '\n'.join(('*' * side_length for _ in range(side_length)))
if __name__ == '__main__':
    print(print_square_pattern(5))