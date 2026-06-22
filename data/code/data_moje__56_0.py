def generate_multiplication_table(n):
    return [[n * i for i in range(1, 11)] for n in [n] for _ in range(1, 11)]

if __name__ == '__main__':
    n = 5
    table = generate_multiplication_table(n)
    print(table)