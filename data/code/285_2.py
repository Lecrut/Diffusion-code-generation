import math
def check_adjacent_pairs(data, tolerance):
    non_compliant_indices = []
    n = len(data)
    for i in range(n - 1):
        diff = abs(data[i] - data[i+1])
        if diff > tolerance:
            non_compliant_indices.append((i, i + 1))
    return non_compliant_indices
if __name__ == '__main__':
    sample_data = [1.000, 1.0005, 2.000, 3.001, 5.0]
    tolerance = 0.001
    result = check_adjacent_pairs(sample_data, tolerance)
    for index1, index2 in result:
        print(f"Non-compliant pair found at indices: ({index1}, {index2})")