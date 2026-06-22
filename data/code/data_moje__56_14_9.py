def generate_multiplication_table(number):
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

if __name__ == '__main__':
    for line in generate_multiplication_table(4):
        print(line)