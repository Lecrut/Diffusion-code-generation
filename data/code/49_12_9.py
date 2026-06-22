def generate_star_grid(size=8):
    return '\n'.join('*' * size for _ in range(size))

if __name__ == '__main__':
    print(generate_star_grid())