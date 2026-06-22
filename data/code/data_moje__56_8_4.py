def get_multiplication_table_6():
    result = {}
    for i in range(1, 11):
        result[i] = 6 * i
    return result

if __name__ == '__main__':
    table = get_multiplication_table_6()
    print(table)