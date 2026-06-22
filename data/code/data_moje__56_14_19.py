def generate_multiplication_table(value: int) -> list[int]:
    return [value * i for i in range(1, 13)]

if __name__ == '__main__':
    result = generate_multiplication_table(4)
    print(result)