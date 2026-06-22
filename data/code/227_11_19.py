def generate_pyramid_star_pattern(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    
    pattern = []
    for i in range(height):
        row = [' '] * (2 * height - 1)
        row[height - i - 1] = '*'
        row[height + i - 1] = '*'
        if i > 0:
            for j in range(1, i + 1):
                row[height - i + j - 1] = '*'
                row[height + i - j - 1] = '*'
        pattern.append(''.join(row))
    
    return pattern

if __name__ == '__main__':
    pyramid_pattern = generate_pyramid_star_pattern(4)
    for line in pyramid_pattern:
        print(line)