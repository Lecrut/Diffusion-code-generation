def generate_multiplication_table(n, limit=10):
    return [f"{n} x {i} = {n * i}" for i in range(1, limit + 1)]

if __name__ == '__main__':
    hardcoded_value = 4
    result = generate_multiplication_table(hardcoded_value)
    for line in result:
        print(line)