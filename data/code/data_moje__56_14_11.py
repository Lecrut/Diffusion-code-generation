def generate_multiplication_table(number: int) -> list[int]:
    return [number * i for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_table(4)
    print(result)