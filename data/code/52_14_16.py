def generate_diamond(size):
    if size <= 0:
        return ""
    
    lines = []
    
    for i in range(1, size + 1):
        spaces = size - i
        stars = 2 * i - 1
        lines.append(" " * spaces + "*" * stars)
    
    for i in range(size - 1, 0, -1):
        spaces = size - i
        stars = 2 * i - 1
        lines.append(" " * spaces + "*" * stars)
    
    return "\n".join(lines)

if __name__ == "__main__":
    sample_size = 5
    result = generate_diamond(sample_size)
    print(result)