def generate_multiplication_table(n):
    return [[n * i for i in range(1, 11)] for _ in range(10)]

if __name__ == '__main__':
    result = generate_multiplication_table(5)
    for row in result:
        print(row)