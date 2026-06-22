def generate_star_pattern(rows=6, cols=6):
    return '\n'.join(('*' * cols for _ in range(rows)))
if __name__ == '__main__':
    print(generate_star_pattern(6, 6))