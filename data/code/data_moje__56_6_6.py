def generate_multiplication_table_9(n):
    for i in range(1, n + 1):
        yield 9 * i

if __name__ == '__main__':
    n = 10
    for row in generate_multiplication_table_9(n):
        print(row)