def get_seven_multiplication_table():
    result = []
    for i in range(1, 11):
        result.append(f"{i} x 7 = {i * 7}")
    return result

if __name__ == '__main__':
    table = get_seven_multiplication_table()
    print(table)