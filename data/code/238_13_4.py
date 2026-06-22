def create_box(width: int, height: int) -> list:
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2")
    
    box = ['#' * width]
    for _ in range(height - 2):
        box.append('#' + ' ' * (width - 2) + '#')
    box.append('#' * width)
    
    return box

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)