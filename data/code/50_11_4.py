def generate_isosceles_triangle(rows):
    if rows <= 0:
        return []
    
    result = []
    max_width = 2 * rows - 1
    half = rows // 2
    
    for i in range(rows):
        stars = 2 * i + 1
        spaces = half - i
        row_str = ' ' * spaces + '*' * stars
        result.append(row_str)
    
    return result

if __name__ == '__main__':
    triangle_lines = generate_isosceles_triangle(5)
    for line in triangle_lines:
        print(line)