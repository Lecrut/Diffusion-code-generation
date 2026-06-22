def generate_nine_table_rows(n):
    return (f"9 * {i} = {9 * i}" for i in range(1, n + 1))

if __name__ == '__main__':
    rows = generate_nine_table_rows(10)
    for row in rows:
        print(row)