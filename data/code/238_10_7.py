def print_box(width=5, height=3):
    if width < 1 or height < 1:
        raise ValueError("Width and height must be greater than zero.")
    
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

if __name__ == '__main__':
    try:
        sample_width = 5
        sample_height = 3
        print_box(sample_width, sample_height)
    except ValueError as e:
        print(e)