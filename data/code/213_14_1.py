from collections import Counter
def process_numbers(data):
    counts = Counter(data)
    sorted_unique_elements = sorted(counts.keys())
    result = []
    for item in sorted_unique_elements:
        result.append((item, counts[item]))
    return result
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 5, 1, 9, 2, 8, 10, 3, 10]
    output = process_numbers(sample_data)
    print(output)