def calculate_multiplication_table(n: int) -> list[int]:
    return [n * i for i in range(1, 11)]

if __name__ == '__main__':
    result = calculate_multiplication_table(8)
    print(result)