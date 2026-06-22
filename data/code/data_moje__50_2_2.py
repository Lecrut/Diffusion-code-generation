def generate_star_triangle(levels=12):
    lines = [' ' * (levels - i) + '*' * (2 * i - 1) for i in range(1, levels + 1)]
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_star_triangle(12)
    print(result)