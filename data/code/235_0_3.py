def generate_right_angled_triangle(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    
    for i in range(1, height + 1):
        print("*" * i)

if __name__ == '__main__':
    try:
        triangle_height = 5
        generate_right_angled_triangle(triangle_height)
    except ValueError as e:
        print(e)