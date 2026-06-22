def multiplication_table_6():
    table = {}
    for i in range(1, 11):
        table[i] = i * 6
    return table

if __name__ == '__main__':
    print(multiplication_table_6())