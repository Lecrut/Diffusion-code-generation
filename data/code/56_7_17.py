def format_multiplication_table(base, limit=10):
    width = len(str(base * limit)) + 1
    results = []
    for i in range(1, limit + 1):
        product = base * i
        line = f"{base:>{width}} x {i:>{width}} = {product:>{width}}"
        results.append(line)
    return "\n".join(results)

if __name__ == '__main__':
    print(format_multiplication_table(5, 10))