def generate_star_square(size=9):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    row = 0
    result = []
    while row < size:
        col = 0
        line = []
        while col < size:
            line.append("*")
            col += 1
        result.append("".join(line))
        row += 1
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_star_square(9))