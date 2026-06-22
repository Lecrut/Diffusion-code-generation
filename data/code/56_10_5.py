def generate_multiplication_table(number):
    return [number * i for i in range(1, 11)]

if __name__ == '__main__':
    target_number = 5
    result = generate_multiplication_table(target_number)
    print(result)