def generate_star_pyramid(n):
    return [('*' * (2 * i + 1)).center(2 * n - 1) for i in range(n)]

if __name__ == '__main__':
    print(generate_star_pyramid(4))