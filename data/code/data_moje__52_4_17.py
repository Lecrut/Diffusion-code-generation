def generate_diamond():
    return '\n'.join(['*' * (9 - 2 * abs(i - 4)) for i in range(9)])

if __name__ == '__main__':
    print(generate_diamond())