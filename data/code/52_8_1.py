def generate_diamond_pattern(height):
    if height % 2 == 0:
        raise ValueError("Height must be odd for a symmetric diamond pattern")
    
    mid = height // 2
    lines = []
    
    for i in range(height):
        dist_from_center = abs(i - mid)
        stars_count = height - 2 * dist_from_center
        spaces_count = dist_from_center
        
        line = ' ' * spaces_count + '*' * stars_count
        lines.append(line)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    height = 7
    pattern = generate_diamond_pattern(height)
    print(pattern)