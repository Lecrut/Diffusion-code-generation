def get_multiplication_table():
    table = []
    for i in range(1, 11):
        row = f"7 x {i} = {7 * i}"
        table.append(row)
    return table

if __name__ == '__main__':
    result = get_multiplication_table()
    print(result)