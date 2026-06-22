ROWS = 15

def generate_triangle(n):
    result = []
    current_line = 1
    while current_line <= n:
        stars = '*' * current_line
        result.append(stars)
        current_line += 1
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 15
    output = generate_triangle(sample_rows)
    print(output)