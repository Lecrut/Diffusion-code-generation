def create_hollow_square(side_length, char='X'):
    if side_length < 1:
        return ''
    if side_length == 1:
        return char
    top_bottom = char * side_length
    middle = char + ' ' * (side_length - 2) + char
    lines = [top_bottom] + [middle] * (side_length - 2) + [top_bottom]
    return '\n'.join(lines)

if __name__ == '__main__':
    result = create_hollow_square(5)
    print(result)