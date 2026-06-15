def generate_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
if __name__ == '__main__':
    generate_multiplication_table(7)
    print("\n" * 2)
    generate_multiplication_table(12)