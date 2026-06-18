def analyze_list(data):
    if not data:
        return None, None, None, None
    total_sum = sum(data)
    total_product = 1
    for x in data:
        total_product *= x
    minimum = min(data)
    maximum = max(data)
    return total_sum, total_product, minimum, maximum
if __name__ == '__main__':
    sample_list = [5, 10, 2, 8, 1]
    s, p, m, x = analyze_list(sample_list)
    print(f"Sum: {s}")
    print(f"Product: {p}")
    print(f"Minimum: {m}")
    print(f"Maximum: {x}")