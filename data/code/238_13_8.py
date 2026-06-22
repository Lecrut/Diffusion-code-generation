def create_box(width, height):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2")
    
    outline = {
        'top_bottom': lambda w: '#' * w,
        'sides': lambda w: '#' + ' ' * (w - 2) + '#'
    }
    
    box = [outline['top_bottom'](width)]
    for _ in range(height - 2):
        box.append(outline['sides'](width))
    box.append(outline['top_bottom'](width))
    
    return box

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)