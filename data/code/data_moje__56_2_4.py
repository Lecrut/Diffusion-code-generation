def multiplication_table_rows(n):
    for i in range(1, 11):
        yield [n * i for j in range(1, i + 1)]

if __name__ == '__main__':
    for row in multiplication_table_rows(5):
        print(row)