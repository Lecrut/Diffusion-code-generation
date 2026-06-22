def generate_multiplication_rows(number, count):
    for i in range(1, count + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == '__main__':
    generate_multiplication_rows(9, 10)