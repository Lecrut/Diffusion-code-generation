HOLLOW_CHAR = "*"
SPACE_CHAR = " "
NEWLINE_CHAR = "\n"
MIN_VALID_SIZE = 1
EDGE_CASE_SIZE = 1

def generate_hollow_square(size):
    if size < 1:
        return ""
    if size == 1:
        return HOLLOW_CHAR
    full_line = HOLLOW_CHAR * size
    if size == 2:
        return NEWLINE_CHAR.join([full_line, full_line])
    empty_line = HOLLOW_CHAR + SPACE_CHAR * (size - EDGE_CASE_SIZE - 1) + HOLLOW_CHAR
    lines = [full_line]
    count = size - 2
    while count > 0:
        lines.append(empty_line)
        count -= 1
    lines.append(full_line)
    return NEWLINE_CHAR.join(lines)

if __name__ == '__main__':
    result = generate_hollow_square(6)
    print(result)