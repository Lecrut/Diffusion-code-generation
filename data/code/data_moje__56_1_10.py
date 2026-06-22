def print_multiplication_table():
    for i in range(1, 13):
        row_values = [f"{i * j:4}" for j in range(1, 13)]
        print("".join(row_values))

if __name__ == '__main__':
    print_multiplication_table()