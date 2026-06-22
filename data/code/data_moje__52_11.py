def generate_diamond(n):
    if n <= 0:
        return ""
    
    top_half = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        top_half.append(spaces + stars)
    
    bottom_half = []
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        bottom_half.append(spaces + stars)
    
    full_pattern = top_half + bottom_half
    return "\n".join(full_pattern)

if __name__ == '__main__':
    size = 5
    result = generate_diamond(size)
    print(result)