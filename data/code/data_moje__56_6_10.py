def generate_nine_table_rows(n_rows):
    for i in range(1, n_rows + 1):
        yield 9 * i

if __name__ == '__main__':
    rows = generate_nine_table_rows(10)
    for row in rows:
        print(row)