def generate_hollow_number_pyramid(rows=5):
    result = []
    if rows <= 0:
        return result
    max_width = (2 * rows) - 1
    for r in range(1, rows + 1):
        num = r
        spaces_out = rows - r
        spaces_in = (2 * r) - 3
        row_str = str(num) + " " * spaces_out
        if r > 1:
            row_str += " " * spaces_in + str(num)
        row_str += " " * spaces_out
        row_centered = row_str.center(max_width)
        result.append(row_centered)
    return "\n".join(result)

if __name__ == '__main__':
    pyramid_output = generate_hollow_number_pyramid(5)
    print(pyramid_output)