def generate_square():
    line = '*' * 7
    return '\n'.join([line] * 7)

if __name__ == '__main__':
    print(generate_square())