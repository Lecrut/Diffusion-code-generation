def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    target_number = 5
    print_multiplication_table(target_number)