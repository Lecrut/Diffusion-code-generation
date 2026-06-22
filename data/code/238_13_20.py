def create_box(width, height):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2")
    
    top_bottom = '#' * width
    middle_line = '#' + ' ' * (width - 2) + '#'
    
    box = [top_bottom]
    for _ in range(height - 2):
        box.append(middle_line)
    box.append(top_bottom)
    
    return box

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)