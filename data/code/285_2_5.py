import math
def check_adjacent_pairs(data):
    non_compliant_indices = []
    for i in range(len(data) - 1):
        diff = abs(data[i] - data[i+1])
        if diff > 0.001:
            non_compliant_indices.append((i, i + 1))
    return non_compliant_indices
if __name__ == '__main__':
    sample_data = [1.0, 1.0005, 2.0, 2.001, 3.0]
    result = check_adjacent_pairs(sample_data)
    for index1, index2 in result:
        print(f"Non-compliant pair found at indices: ({index1}, {index2})")