import sys
def find_adjacent_inequalities(data):
    results = []
    n = len(data)
    if n < 2:
        return results
    for i in range(n - 1):
        if data[i] != data[i+1]:
            results.append((i, data[i], data[i+1]))
    return results
if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 5, 5, 4, 1]
    inequalities = find_adjacent_inequalities(sample_list)
    for index, val1, val2 in inequalities:
        print(f"Index: {index}, Comparing: {val1} and {val2}")