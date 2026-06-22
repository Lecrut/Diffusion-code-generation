def generate_multiplication_table():
    header = "{:>4}".format("x")
    for j in range(1, 13):
        header += "{:>4}".format(j)
    print(header)
    separator = "-" * (4 + 4 * 12)
    print(separator)
    for i in range(1, 13):
        row = "{:>4}".format(i)
        for j in range(1, 13):
            row += "{:>4}".format(i * j)
        print(row)

if __name__ == '__main__':
    generate_multiplication_table()