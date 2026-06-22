def generate_multiplication_table(factor):
    return [factor * i for i in range(1, 11)]

if __name__ == '__main__':
    print(generate_multiplication_table(4))