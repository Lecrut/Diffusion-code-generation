def create_hollow_square(side, char='X'):
    if side < 1:
        return ""
    if side == 1:
        return char
    top_bottom = char * side
    middle = char + ' ' * (side - 2) + char
    lines = [top_bottom]
    for _ in range(side - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = create_hollow_square(5, 'X')
    print(result)