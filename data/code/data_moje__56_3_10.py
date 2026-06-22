def generate_multiplication_table(n, count=10):
    return [f"{n} x {i} = {n * i}" for i in range(1, count + 1)]

if __name__ == '__main__':
    result = generate_multiplication_table(7)
    for line in result:
        print(line)