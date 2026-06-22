def generate_star_square(size=4):
    return ['*' * size for _ in range(size)]
if __name__ == '__main__':
    result = generate_star_square()
    print(result)