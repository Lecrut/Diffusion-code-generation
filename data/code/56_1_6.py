def print_multiplication_table():
    for i in range(1, 13):
        line = ""
        for j in range(1, 13):
            value = i * j
            line += f"{value:4d}"
        print(line)

if __name__ == '__main__':
    print_multiplication_table()