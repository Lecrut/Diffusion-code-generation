def get_multiplication_table_7():
    result = []
    for i in range(1, 11):
        result.append(f"7 x {i} = {7 * i}")
    return result

if __name__ == '__main__':
    table = get_multiplication_table_7()
    print(table)