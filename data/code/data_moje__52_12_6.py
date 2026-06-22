def create_diamond(radius):
    if radius <= 0:
        return ""
    
    def validate_radius(r):
        if not isinstance(r, int):
            raise TypeError("Radius must be an integer")
        if r <= 0:
            raise ValueError("Radius must be positive")
        return r
    
    valid_radius = validate_radius(radius)
    
    half_lines = []
    for i in range(1, valid_radius + 1):
        spaces_count = valid_radius - i
        stars_count = 2 * i - 1
        half_lines.append(' ' * spaces_count + '*' * stars_count)
    
    all_lines = half_lines + half_lines[-2::-1]
    
    return '\n'.join(all_lines)

if __name__ == '__main__':
    radius_value = 4
    diamond_result = create_diamond(radius_value)
    print(diamond_result)