def get_multiplication_table():
    number = 9
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = get_multiplication_table()
    for line in result:
        print(line)