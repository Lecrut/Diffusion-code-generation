def generate_triangle(base):
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    
    return '\n'.join('*' * i for i in range(1, base + 1))

if __name__ == '__main__':
    triangle = generate_triangle(10)
    print(triangle)