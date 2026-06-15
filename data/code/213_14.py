import collections
def analyze_list(data):
    counts = collections.Counter(data)
    unique_sorted_elements = sorted(counts.keys())
    result = []
    for element in unique_sorted_elements:
        result.append((element, counts[element]))
    return result
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 1, 9, 2, 10, 5, 3]
    output = analyze_list(sample_list)
    print(output)