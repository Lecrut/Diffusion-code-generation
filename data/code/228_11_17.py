def generate_triangle(base):
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    
    triangle = []
    for i in range(1, base + 1):
        triangle.append('*' * i)
    return '\n'.join(triangle)

if __name__ == '__main__':
    print(generate_triangle(10))