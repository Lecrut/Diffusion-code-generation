import collections
def analyze_list(data):
    counts = collections.Counter(data)
    sorted_unique_elements = sorted(counts.keys())
    result = []
    for item in sorted_unique_elements:
        result.append((item, counts[item]))
    return result
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 1, 5, 9, 2, 8, 10, 5]
    output = analyze_list(sample_data)
    print(output)