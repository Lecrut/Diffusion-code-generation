def generate_diamond_star_pattern(height):
    if height % 2 == 0:
        odd_height = height + 1
    else:
        odd_height = height
    
    max_width = odd_height
    middle = odd_height // 2
    
    lines = []
    
    for i in range(odd_height):
        distance_from_center = abs(i - middle)
        stars_needed = max_width - (2 * distance_from_center)
        spaces_needed = distance_from_center
        
        line = ' ' * spaces_needed + '*' * stars_needed
        lines.append(line)
        
    return '\n'.join(lines)

if __name__ == '__main__':
    pattern_height = 7
    result = generate_diamond_star_pattern(pattern_height)
    print(result)