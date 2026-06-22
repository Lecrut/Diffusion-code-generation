def generate_diamond_pattern(size: int) -> str:
    lines = []
    upper_range = range(size, 0, -1)
    lower_range = range(1, size + 1)
    all_ranges = (upper_range, lower_range)
    
    for current_range in all_ranges:
        for row in current_range:
            spaces = ' ' * (size - row)
            stars = '*' * (2 * row - 1)
            lines.append(spaces + stars)
            
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond_pattern(5))