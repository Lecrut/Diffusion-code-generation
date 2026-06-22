def generate_star_square(size=12):
    row = "* " * size
    return "\n".join([row] * size)

if __name__ == '__main__':
    print(generate_star_square(12))