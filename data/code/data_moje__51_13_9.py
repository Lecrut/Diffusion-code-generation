def render_number_pyramid(rows):
    max_width = rows * 2 - 1
    result = []
    for r in range(1, rows + 1):
        sequence = list(range(1, r + 1)) + list(range(r - 1, 0, -1))
        spaces_count = max_width // 2 - (r - 1)
        spaces = ' ' * spaces_count
        line = spaces + ' '.join(str(x) for x in sequence)
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 8
    print(render_number_pyramid(sample_rows))