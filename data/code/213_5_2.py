import math
def analyze_sequence(data):
    if not data:
        return 0, 1, 0.0
    n = len(data)
    total_sum = sum(data)
    total_product = 1
    for x in data:
        total_product *= x
    mean = total_sum / n
    variance = sum([(x - mean) ** 2 for x in data]) / n
    return total_sum, total_product, variance
if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5]
    total_sum, total_product, variance = analyze_sequence(input_sequence)
    print(f"Sum: {total_sum}")
    print(f"Product: {total_product}")
    print(f"Variance: {variance}")