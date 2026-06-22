def generate_multiplication_table_rows(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == '__main__':
    generate_multiplication_table_rows(9)