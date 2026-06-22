def generate_multiplication_table(number, limit=10):
    results = []
    for i in range(1, limit + 1):
        results.append(f"{number} x {i} = {number * i}")
    return results

if __name__ == '__main__':
    target_number = 5
    table = generate_multiplication_table(target_number)
    for line in table:
        print(line)