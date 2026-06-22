def render_square_pattern(side_length):
    lines = []
    for _ in range(side_length):
        line = '*' * side_length
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    side_length = 7
    result = render_square_pattern(side_length)
    print(result)