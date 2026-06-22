def hollow_square(side_length, char='X'):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return char
    rows = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            rows.append(char * side_length)
        else:
            rows.append(char + ' ' * (side_length - 2) + char)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(hollow_square(5, 'X'))