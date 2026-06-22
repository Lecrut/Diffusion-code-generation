def create_box(width, height):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2")
    
    top_bottom = ['#' * width]
    middle_lines = ['#' + ' ' * (width - 2) + '#'] * (height - 2)
    
    return top_bottom + middle_lines + top_bottom

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)