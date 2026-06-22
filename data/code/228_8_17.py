def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    for i in range(1, n + 1):
        yield ' '.join(str(j) for j in range(1, i + 1))

if __name__ == '__main__':
    pattern = triangle_pattern(5)
    for row in pattern:
        print(row)