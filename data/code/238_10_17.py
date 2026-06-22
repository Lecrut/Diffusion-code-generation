def generate_box(width=5, height=3):
    if width < 2 or height < 1:
        raise ValueError("Invalid dimensions for box")
    
    box = []
    for i in range(height):
        if i == 0 or i == height - 1:
            row = '*' * width
        else:
            row = '*' + ' ' * (width - 2) + '*'
        box.append(row)
    return '\n'.join(box)

if __name__ == '__main__':
    print(generate_box())