STAR_PATTERN_HEIGHT = 5

def generate_star_triangle(height=STAR_PATTERN_HEIGHT):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(generate_star_triangle())