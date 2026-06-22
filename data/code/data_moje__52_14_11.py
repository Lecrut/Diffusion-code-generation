def diamond_star_pattern(size: int = 5) -> str:
    if size < 1:
        return ""
    
    lines = []
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = diamond_star_pattern(5)
    print(result)