def generate_square(size=7):
    return (*('*' * size + '\n',) * size,)

if __name__ == '__main__':
    result = generate_square(7)
    print(''.join(result))