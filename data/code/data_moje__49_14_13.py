def generate_star_square(side_length=7):
    return '\n'.join('*' * side_length for _ in range(side_length))

if __name__ == '__main__':
    print(generate_star_square(7))