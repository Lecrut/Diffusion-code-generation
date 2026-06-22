def generate_right_triangle(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(generate_right_triangle(5))