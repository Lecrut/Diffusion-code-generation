import collections
def analyze_list(data):
    counts = collections.Counter(data)
    sorted_unique_elements = sorted(counts.keys())
    result = []
    for element in sorted_unique_elements:
        result.append((element, counts[element]))
    return result
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 1, 9, 2, 3, 8, 10, 2]
    output = analyze_list(sample_list)
    print(output)