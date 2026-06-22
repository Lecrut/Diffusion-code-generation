def generate_hollow_square(side_length, char):
    lines = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            line = char * side_length
        else:
            line = char + ' ' * (side_length - 2) + char
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    side = 5
    symbol = 'X'
    result = generate_hollow_square(side, symbol)
    print(result)