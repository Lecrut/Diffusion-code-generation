def multiplication_table(n, rows):
    results = []
    for i in range(1, rows + 1):
        results.append(f"{n} x {i} = {n * i}")
    return results

if __name__ == '__main__':
    n = 3
    rows = 10
    output = multiplication_table(n, rows)
    for line in output:
        print(line)