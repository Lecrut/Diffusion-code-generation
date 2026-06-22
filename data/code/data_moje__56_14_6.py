def generate_multiplication_table(n: int) -> list[list[int]]:
    return [[n * j for j in range(1, 11)] for _ in range(1)]

if __name__ == '__main__':
    table = generate_multiplication_table(4)
    for row in table:
        print(row)