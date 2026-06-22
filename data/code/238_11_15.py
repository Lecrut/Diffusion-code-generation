def create_hollow_square(side_length):
    if side_length < 2:
        raise ValueError("Side length must be at least 2")
    
    square = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            square.append('*' * side_length)
        else:
            square.append('*' + ' ' * (side_length - 2) + '*')
    return '\n'.join(square)

if __name__ == '__main__':
    try:
        sample_side_length = 4
        print(create_hollow_square(sample_side_length))
    except ValueError as e:
        print(e)