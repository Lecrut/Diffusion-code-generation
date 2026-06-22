def generate_multiplication_table(number):
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result

if __name__ == '__main__':
    table = generate_multiplication_table(5)
    for line in table:
        print(line)