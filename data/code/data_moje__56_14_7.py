def generate_multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_table(4)
    for line in result:
        print(line)