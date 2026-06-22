def generate_multiplication_table(n, size=10):
    return [[n * i for i in range(1, size + 1)]]

if __name__ == '__main__':
    print(generate_multiplication_table(4))