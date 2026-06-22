def print_multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]

if __name__ == '__main__':
    for line in print_multiplication_table(5):
        print(line)