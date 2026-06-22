def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_pattern(n):
    if n < 1:
        raise ValueError("Number of rows must be at least 1")
    for i in range(1, n + 1):
        yield ' '.join(str(j) for j in range(1, i + 1))

if __name__ == '__main__':
    for row in triangle_pattern(5):
        print(row)