def get_diamond_pattern(half_height):
    lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    
    upper_part = lines[:-1]
    lower_part = lines[::-1]
    
    return upper_part + lower_part

if __name__ == '__main__':
    result = get_diamond_pattern(4)
    for line in result:
        print(line)