def print_star_square(size):
    EMPTY_SPACE = ' '
    STAR_CHAR = '*'
    if size <= 0:
        return ""
    if size == 1:
        return STAR_CHAR
    FULL_ROW = STAR_CHAR * size
    MIDDLE_ROW = STAR_CHAR + EMPTY_SPACE * (size - 2) + STAR_CHAR
    rows = [FULL_ROW]
    for _ in range(size - 2):
        rows.append(MIDDLE_ROW)
    rows.append(FULL_ROW)
    return "\n".join(rows)

if __name__ == '__main__':
    print(print_star_square(1))
    print()
    print(print_star_square(5))
    print()
    print(print_star_square(8))