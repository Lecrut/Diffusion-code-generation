def generate_nine_table():
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_nine_table()
    for line in result:
        print(line)