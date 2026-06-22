def generate_multiplication_table(number, count):
    return [(i, number, i * number) for i in range(1, count + 1)]

if __name__ == '__main__':
    rows = generate_multiplication_table(3, 10)
    for row in rows:
        print(f"{row[0]} x {row[1]} = {row[2]}")