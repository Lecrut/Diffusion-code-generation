def generate_box(height, width):
    if height < 1 or width < 1:
        raise ValueError("Height and width must be greater than zero.")
    
    box = '@' * width + '\n'
    box += ('@' * width + '\n') * (height - 2)
    box += '@' * width
    return box

if __name__ == '__main__':
    height, width = 3, 2
    if height < 1 or width < 1:
        print("Invalid dimensions. Height and width must be greater than zero.")
    else:
        result = generate_box(height, width)
        print(result)