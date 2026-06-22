def generate_star_triangle(height):
    return '\n'.join(' ' * (height - i) + '*' * (2 * i - 1) for i in range(1, height + 1))

if __name__ == '__main__':
    print(generate_star_triangle(6))