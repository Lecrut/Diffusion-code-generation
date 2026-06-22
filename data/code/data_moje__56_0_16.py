def generate_multiplication_table(n):
    return [[n * i for i in range(1, 11)] for _ in range(1, 11)]

if __name__ == '__main__':
    print(generate_multiplication_table(7))