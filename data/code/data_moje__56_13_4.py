def get_nine_multiplication_table():
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

if __name__ == "__main__":
    table = get_nine_multiplication_table()
    for row in table:
        print(row)