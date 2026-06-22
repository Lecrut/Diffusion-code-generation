def generate_diamond(size):
    if size <= 0:
        return ""
    
    half = size // 2
    
    lines = []
    
    for i in range(half + 1):
        spaces = half - i
        stars = 2 * i + 1
        lines.append(" " * spaces + "*" * stars)
    
    for i in range(half - 1, -1, -1):
        spaces = half - i
        stars = 2 * i + 1
        lines.append(" " * spaces + "*" * stars)
    
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))