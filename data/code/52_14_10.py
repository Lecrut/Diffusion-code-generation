def generate_diamond_pattern(size: int) -> str:
    if size <= 0:
        return ""
    
    lines = []
    half = size - 1
    
    for i in range(size):
        spaces = half - i
        stars = 1 + 2 * i
        line = " " * spaces + "*" * stars
        lines.append(line)
    
    for i in range(size - 2, -1, -1):
        spaces = half - i
        stars = 1 + 2 * i
        line = " " * spaces + "*" * stars
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = generate_diamond_pattern(sample_size)
    print(result)