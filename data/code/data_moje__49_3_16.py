HOLLOW_STAR = '*'
SPACE_CHAR = ' '
DEFAULT_SIZE = 6

def create_hollow_square(size: int) -> str:
    if size < 1:
        return SPACE_CHAR
    if size == 1:
        return HOLLOW_STAR
    top_bottom_row = HOLLOW_STAR * size
    middle_row = HOLLOW_STAR + (SPACE_CHAR * (size - 2)) + HOLLOW_STAR
    lines = [top_bottom_row]
    for _ in range(size - 2):
        lines.append(middle_row)
    lines.append(top_bottom_row)
    return "\n".join(lines)

if __name__ == '__main__':
    output = create_hollow_square(DEFAULT_SIZE)
    print(output)