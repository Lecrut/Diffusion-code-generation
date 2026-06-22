def print_asterisk_square(size: int) -> str:
    line = "*" * size
    square = (line + "\n") * size
    return square.rstrip("\n")

if __name__ == '__main__':
    result = print_asterisk_square(7)
    print(result)