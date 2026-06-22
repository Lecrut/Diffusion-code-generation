def get_multiplication_table():
    header = "{:>5}".format(" ")
    for j in range(1, 13):
        header += "{:>5}".format(j)
    print(header)
    print("-" * 61)
    for i in range(1, 13):
        row = "{:>5}".format(i)
        for j in range(1, 13):
            row += "{:>5}".format(i * j)
        print(row)

if __name__ == '__main__':
    result = get_multiplication_table()