def multiplication_table_rows(n):
    for i in range(1, 11):
        yield [n * j for j in range(1, 11)]

if __name__ == '__main__':
    sample_number = 7
    for row in multiplication_table_rows(sample_number):
        print(row)