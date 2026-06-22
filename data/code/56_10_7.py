def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == '__main__':
    target_number = 5
    print_multiplication_table(target_number)