def generate_diamond_pattern(height: int) -> list[str]:
    if height <= 0:
        return []
    if height % 2 == 0:
        half = height // 2
    else:
        half = (height + 1) // 2
    
    top_half = [f"{' ' * (half - i)}{'*' * (2 * i - 1)}" for i in range(1, half + 1)]
    bottom_half = top_half[-2::-1] if half > 1 else []
    return top_half + bottom_half

if __name__ == '__main__':
    sample_height = 7
    result = generate_diamond_pattern(sample_height)
    for line in result:
        print(line)