def generate_diamond(n):
    if n <= 0:
        return ""
    
    lines = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    
    return "\n".join(lines)

if __name__ == '__main__':
    size = 5
    result = generate_diamond(size)
    print(result)