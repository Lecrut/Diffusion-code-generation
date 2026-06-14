import math
def analyze_sequence(data):
    if not data:
        return 0, 0, 0
    n = len(data)
    s = sum(data)
    p = 1
    for x in data:
        p *= x
    mean = s / n
    variance = sum([(x - mean) ** 2 for x in data]) / n
    return s, p, variance
if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5]
    total_sum, total_product, variance = analyze_sequence(input_sequence)
    print(f"Sum: {total_sum}")
    print(f"Product: {total_product}")
    print(f"Variance: {variance}")