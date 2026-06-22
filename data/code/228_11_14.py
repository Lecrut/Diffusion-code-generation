def generate_triangle(base):
    triangle_art = []
    for i in range(1, base + 1):
        triangle_art.append('*' * i)
    return '\n'.join(triangle_art)

if __name__ == '__main__':
    print(generate_triangle(10))