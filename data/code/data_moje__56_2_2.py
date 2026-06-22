def multiplication_table_rows(n):
    for i in range(1, n + 1):
        yield [i * j for j in range(1, 11)]

if __name__ == '__main__':
    n = 5
    for row in multiplication_table_rows(n):
        print(row)