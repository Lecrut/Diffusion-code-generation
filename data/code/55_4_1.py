def generate_pyramid(size):
    return [
        [(chr(65 + abs(i - j)) for i in range(size - row - 1)) +
         [(chr(65 + row))] +
         [(chr(65 + abs(i - j)) for i in range(size - row - 1))]
         for j in range(2 * row + 1)]
        for row in range(size)
    ]

def format_pyramid(grid):
    lines = []
    for row in grid:
        line_parts = []
        for col in row:
            if isinstance(col, str):
                line_parts.append(col)
            else:
                line_parts.extend(list(col))
        lines.append(" ".join(line_parts))
    return "\n".join(lines)

if __name__ == '__main__':
    size = 5
    pyramid = generate_pyramid(size)
    result = format_pyramid(pyramid)
    print(result)