def print_multiplication_table(number, start=1, end=10):
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == '__main__':
    print_multiplication_table(5)