def generate_centered_triangle(levels):
    return '\n'.join([' ' * (levels - i - 1) + '*' * (2 * i + 1) for i in range(levels)])

if __name__ == '__main__':
    print(generate_centered_triangle(12))