import collections
def analyze_list(data):
    counts = collections.Counter(data)
    unique_sorted = sorted(counts.keys())
    result = []
    for item in unique_sorted:
        result.append((item, counts[item]))
    return result
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 5, 1, 9, 2, 5, 3, 8, 10, 2]
    output = analyze_list(sample_data)
    print(output)