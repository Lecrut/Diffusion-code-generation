NUM_ROWS = 15
STAR_CHAR = '*'

def render_triangle(height: int) -> list[str]:
    lines: list[str] = []
    row_num = 1
    while row_num <= height:
        line = STAR_CHAR * row_num
        lines.append(line)
        row_num += 1
    return lines

def main():
    result = render_triangle(NUM_ROWS)
    for line in result:
        print(line)

if __name__ == '__main__':
    main()