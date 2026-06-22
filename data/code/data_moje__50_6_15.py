def build_symmetric_triangle(height):
    max_width = height * 2 - 1
    top_half = []
    for row_index in range(1, height + 1):
        star_count = row_index * 2 - 1
        padding = (max_width - star_count) // 2
        row_str = ' ' * padding + '*' * star_count + ' ' * padding
        top_half.append(row_str)
    bottom_half = top_half[-2::-1]
    full_lines = top_half + bottom_half
    return '\n'.join(full_lines)

if __name__ == '__main__':
    triangle_height = 5
    result = build_symmetric_triangle(triangle_height)
    print(result)