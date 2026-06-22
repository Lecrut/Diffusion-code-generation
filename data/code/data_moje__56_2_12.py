def multiplication_table_generator(n):
    for i in range(1, 11):
        yield [n * j for j in range(1, i + 1)]

if __name__ == '__main__':
    n = 5
    for row in multiplication_table_generator(n):
        print(row)