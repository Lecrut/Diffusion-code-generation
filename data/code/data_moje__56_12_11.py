def get_multiplication_table_rows(factor, count):
    return [f"{factor} x {i} = {factor * i}" for i in range(1, count + 1)]

if __name__ == '__main__':
    factor = 3
    count = 10
    rows = get_multiplication_table_rows(factor, count)
    for row in rows:
        print(row)