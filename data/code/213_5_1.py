import math
def analyze_sequence(data):
    if not data:
        return 0, 0, 0
    n = len(data)
    total_sum = sum(data)
    total_product = 1
    for x in data:
        total_product *= x
    mean = total_sum / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return total_sum, total_product, variance
if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5]
    data_to_analyze = input_sequence
    s, p, v = analyze_sequence(data_to_analyze)
    print(f"Sum: {s}")
    print(f"Product: {p}")
    print(f"Variance: {v}")