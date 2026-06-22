def hollow_square(side_length, character):
    if side_length < 1:
        return ""
    if side_length == 1:
        return character
    top_bottom = character * side_length
    middle = character + ' ' * (side_length - 2) + character
    lines = [top_bottom]
    if side_length > 2:
        lines.extend([middle] * (side_length - 2))
    lines.append(top_bottom)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = hollow_square(5, 'X')
    print(result)