def get_multiplication_table(n, rows=10):
    result = []
    for i in range(1, rows + 1):
        result.append(f"{n} x {i} = {n * i}")
    return result

if __name__ == '__main__':
    result = get_multiplication_table(3)
    for line in result:
        print(line)