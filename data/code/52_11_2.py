def generate_diamond_pattern(width: int) -> str:
    if width <= 0 or width % 2 == 0:
        raise ValueError("Width must be a positive odd integer")
    
    mid = width // 2
    lines = []
    
    for i in range(width):
        distance = abs(mid - i)
        stars_count = width - 2 * distance
        spaces_count = distance
        
        row = ' ' * spaces_count + '*' * stars_count + ' ' * spaces_count
        lines.append(row)
        
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(7)
    print(result)