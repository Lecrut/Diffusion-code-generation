def generate_nine_multiplication():
    for i in range(1, 11):
        yield (i, 9 * i)

if __name__ == '__main__':
    for factor, product in generate_nine_multiplication():
        print(product)