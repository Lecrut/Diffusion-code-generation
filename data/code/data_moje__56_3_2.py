def get_multiplication_table_7():
    table = []
    for i in range(1, 11):
        result = 7 * i
        table.append(f"7 x {i} = {result}")
    return table

if __name__ == '__main__':
    output = get_multiplication_table_7()
    print(output)