def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    
    SQUARE_TOP_BOTTOM = '*' * side_length
    SQUARE_SIDES = '*' + ' ' * (side_length - 2) + '*'
    
    square = [SQUARE_TOP_BOTTOM]
    for _ in range(side_length - 2):
        square.append(SQUARE_SIDES)
    square.append(SQUARE_TOP_BOTTOM)
    
    return '\n'.join(square)

if __name__ == '__main__':
    sample_side_length = 4
    print(create_hollow_square(sample_side_length))