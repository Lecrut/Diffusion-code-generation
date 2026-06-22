def generate_multiplication_table_rows_9():
    for i in range(1, 11):
        yield 9 * i

if __name__ == '__main__':
    rows = list(generate_multiplication_table_rows_9())
    print(rows)