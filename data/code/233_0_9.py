def create_rectangle(width=5, height=5, char='*'):
    if width < 1 or height < 1:
        raise ValueError("Width and height must be greater than zero")
    
    rectangle = [[char for _ in range(width)] for _ in range(height)]
    return rectangle

def print_rectangle(rectangle):
    for row in rectangle:
        print(''.join(row))

if __name__ == '__main__':
    rect = create_rectangle()
    print_rectangle(rect)