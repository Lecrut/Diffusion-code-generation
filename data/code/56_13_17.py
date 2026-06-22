def get_nine_multiplication_table():
    result = []
    for i in range(1, 11):
        result.append(f"9 x {i} = {i * 9}")
    return result

if __name__ == '__main__':
    table = get_nine_multiplication_table()
    for line in table:
        print(line)