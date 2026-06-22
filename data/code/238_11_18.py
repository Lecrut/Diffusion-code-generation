def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    square = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            square.append('*' * side_length)
        else:
            square.append('*' + ' ' * (side_length - 2) + '*')
    return '\n'.join(square)

if __name__ == '__main__':
    sample_side_length = 4
    result = create_hollow_square(sample_side_length)
    print(result)