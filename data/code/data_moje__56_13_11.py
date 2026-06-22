def get_multiplication_table():
    number = 9
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result

if __name__ == '__main__':
    table = get_multiplication_table()
    for line in table:
        print(line)