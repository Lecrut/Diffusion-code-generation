from collections import Counter

def count_and_sort_strings(strings):
    string_counts = Counter(strings)
    sorted_counts = dict(sorted(string_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_and_sort_strings(sample_strings))