def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        raise ValueError("Center width must be odd for a symmetric diamond")
    
    half = center_width // 2
    lines = []
    
    top_half = [
        ' ' * (half - i) + '*' * (2 * i + 1)
        for i in range(half + 1)
    ]
    
    bottom_half = [
        ' ' * (i + 1) + '*' * (2 * (half - i) - 1)
        for i in range(half)
    ]
    
    lines = top_half + bottom_half
    return '\n'.join(lines)

if __name__ == '__main__':
    pattern = generate_diamond_pattern(9)
    print(pattern)