def get_multiplication_table_9():
    return [f"{i} x 9 = {i * 9}" for i in range(1, 11)]

if __name__ == '__main__':
    table = get_multiplication_table_9()
    print(table)