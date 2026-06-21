from collections import Counter

def count_and_sort_strings(strings):
    counts = Counter(strings)
    sorted_counts = dict(counts.most_common())
    return sorted_counts

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_and_sort_strings(sample_strings)
    print(result)