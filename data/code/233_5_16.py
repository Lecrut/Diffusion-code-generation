def create_rectangle(width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    rectangle = []
    for _ in range(height):
        row = ['X'] * width
        rectangle.append(''.join(row))
    
    return '\n'.join(rectangle)

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 3
    print(create_rectangle(WIDTH, HEIGHT))