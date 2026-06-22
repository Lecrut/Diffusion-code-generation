def generate_square_pattern(size=12):
    star_row = "* " * size
    return "\n".join([star_row] * size)

if __name__ == '__main__':
    print(generate_square_pattern())