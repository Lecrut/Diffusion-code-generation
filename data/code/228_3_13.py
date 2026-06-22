def generate_right_triangle(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    
    return '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, height + 1))

if __name__ == '__main__':
    print(generate_right_triangle(5))