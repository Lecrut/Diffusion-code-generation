def generate_inverted_triangle(height):
    rows = []
    for i in range(height, 0, -1):
        stars = '*' * i
        rows.append(stars)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_inverted_triangle(5))