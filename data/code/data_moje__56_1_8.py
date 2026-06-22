def print_multiplication_table():
    header = "x".rjust(4)
    for i in range(1, 13):
        header += str(i).rjust(5)
    print(header)
    for row_num in range(1, 13):
        row_values = [str(row_num * col_num).rjust(4) for col_num in range(1, 13)]
        print(f"{str(row_num).rjust(4)} {''.join(row_values)}")

if __name__ == '__main__':
    print_multiplication_table()