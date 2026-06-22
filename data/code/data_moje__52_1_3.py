def build_diamond_pattern(size):
    if not isinstance(size, int) or size < 1 or size % 2 == 0:
        raise ValueError("Size must be a positive odd integer")
    
    def create_line(spaces, stars):
        return " " * spaces + "*" * stars
    
    center = size // 2
    lines = []
    for row in range(size):
        distance = abs(row - center)
        star_count = size - 2 * distance
        space_count = distance
        lines.append(create_line(space_count, star_count))
    
    return "\n".join(lines)

if __name__ == '__main__':
    pattern = build_diamond_pattern(7)
    print(pattern)