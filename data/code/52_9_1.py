def generate_diamond(half_height: int) -> list[str]:
    lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
        
    return lines

if __name__ == '__main__':
    half_height = 4
    result = generate_diamond(half_height)
    for line in result:
        print(line)