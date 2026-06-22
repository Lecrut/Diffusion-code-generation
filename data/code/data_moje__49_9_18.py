def print_square_pattern(size=12):
    row = "* " * size
    lines = [row] * size
    return "\n".join(lines)

if __name__ == '__main__':
    result = print_square_pattern(12)
    print(result)