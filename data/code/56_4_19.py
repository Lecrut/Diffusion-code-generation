def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == '__main__':
    print_multiplication_table(5)