def create_right_triangle(height):
    if height <= 0:
        raise ValueError("Height must be a positive integer")
    
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(create_right_triangle(5))