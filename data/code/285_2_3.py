import math
def check_adjacent_pairs(data, tolerance):
    non_compliant_indices = []
    n = len(data)
    for i in range(n - 1):
        if abs(data[i] - data[i+1]) > tolerance:
            non_compliant_indices.append((i, i + 1))
    return non_compliant_indices
if __name__ == '__main__':
    sample_data = [1.0, 1.0005, 2.0, 2.001, 5.0, 5.002]
    tolerance = 0.001
    result = check_adjacent_pairs(sample_data, tolerance)
    for index1, index2 in result:
        print(f"Non-compliant pair found at indices: ({index1}, {index2})")