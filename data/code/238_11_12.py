def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    
    top_bottom = '*' * side_length
    middle_lines = ['*' + ' ' * (side_length - 2) + '*'] * (side_length - 2)
    
    square = [top_bottom] + middle_lines + [top_bottom]
    return '\n'.join(square)

if __name__ == '__main__':
    sample_side_length = 4
    print(create_hollow_square(sample_side_length))