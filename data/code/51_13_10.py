import math

def render_symmetric_number_pyramid(rows):
    result = []
    for current_row in range(1, rows + 1):
        spaces = ' ' * (rows - current_row)
        ascending = ''.join(str(i) for i in range(1, current_row + 1))
        descending = ''.join(str(i) for i in range(current_row - 1, 0, -1))
        line = spaces + ascending + descending
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    rows = 8
    output = render_symmetric_number_pyramid(rows)
    print(output)