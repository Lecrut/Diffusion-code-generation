def generate_hollow_square(side_length):
    if side_length < 1:
        return ""
    rows = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            rows.append('X' * side_length)
        else:
            row = 'X' + ' ' * (side_length - 2) + 'X'
            rows.append(row)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))