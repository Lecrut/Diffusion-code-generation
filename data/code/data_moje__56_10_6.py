def generate_multiplication_table(number):
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_table(5)
    for line in result:
        print(line)