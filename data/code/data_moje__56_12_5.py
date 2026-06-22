def get_multiplication_table(number, count):
    return [f"{i} x {number} = {i * number}" for i in range(1, count + 1)]

if __name__ == '__main__':
    number = 3
    count = 10
    results = get_multiplication_table(number, count)
    for row in results:
        print(row)