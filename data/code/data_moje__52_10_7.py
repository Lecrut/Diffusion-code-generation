def generate_diamond(size: int) -> str:
    if size <= 0:
        return ""
    
    half = size // 2
    lines = []
    
    for i in range(-half, half + 1):
        spaces = abs(i)
        stars = size - 2 * spaces
        line = " " * spaces + "*" * stars
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == "__main__":
    result = generate_diamond(5)
    print(result)