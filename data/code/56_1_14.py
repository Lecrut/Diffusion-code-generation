def print_multiplication_table():
    for i in range(1, 13):
        row = ""
        for j in range(1, 13):
            row += f"{i} x {j} = {i * j:>3}"
            if j < 13:
                row += "  "
        print(row)

if __name__ == '__main__':
    print_multiplication_table()