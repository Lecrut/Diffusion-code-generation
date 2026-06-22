SYMMETRY_MAP = {
    'shape': 'triangle',
    'base_width': 2,
    'offset': 1,
    'pattern': 'symmetric'
}

def create_symmetric_star_triangle(height):
    if height < 1:
        return []
    max_stars = (height * 2) - 1
    current_stars = SYMMETRY_MAP['base_width']
    result = []
    while current_stars <= max_stars:
        padding = (max_stars - current_stars) // 2
        row = ' ' * padding + '*' * current_stars + ' ' * padding
        result.append(row)
        current_stars += 2
    upper_height = len(result)
    lower_part = result[:-1][::-1]
    return result + lower_part

if __name__ == '__main__':
    sample_height = 6
    triangle_rows = create_symmetric_star_triangle(sample_height)
    print('\n'.join(triangle_rows))