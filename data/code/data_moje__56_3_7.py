def get_multiplication_table():
    result = []
    for i in range(1, 11):
        row = [f"{7} x {i} = {7 * i}" for i in range(1, 11)]
        result.append(" | ".join(row))
    return result

if __name__ == '__main__':
    table = get_multiplication_table()
    for row in table:
        print(row)