def get_multiplication_table_9():
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = get_multiplication_table_9()
    for line in result:
        print(line)