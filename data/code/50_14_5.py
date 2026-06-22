def generate_diamond_pattern(width):
    if width <= 0:
        return ""
    if width % 2 == 0:
        return generate_diamond_pattern(width + 1)
    
    half = width // 2
    lines = []
    
    for i in range(width):
        if i <= half:
            spaces = half - i
            stars = 1 + 2 * i
        else:
            spaces = i - half
            stars = width - 2 * spaces
        
        line = " " * spaces + "*" * stars + " " * spaces
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_width = 11
    result = generate_diamond_pattern(sample_width)
    print(result)