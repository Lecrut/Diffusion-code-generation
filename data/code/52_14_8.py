def generate_diamond(n):
    if n <= 0:
        return ""
    
    lines = []
    mid = n // 2
    
    for i in range(n):
        diff = abs(i - mid)
        spaces = " " * diff
        stars = "*" * (n - 2 * diff)
        lines.append(spaces + stars)
        
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))