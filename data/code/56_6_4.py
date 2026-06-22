def get_nine_multiplication_table():
    return (f"{i} * 9 = {i * 9}" for i in range(1, 11))

if __name__ == '__main__':
    for row in get_nine_multiplication_table():
        print(row)