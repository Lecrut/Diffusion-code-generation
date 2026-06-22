def generate_nine_multiplication_table():
    return [f"{i} x 9 = {i * 9}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_nine_multiplication_table()
    for line in result:
        print(line)