from collections import Counter

def count_and_sort_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All items in the list must be strings")
    
    string_counts = Counter(strings)
    sorted_string_counts = dict(sorted(string_counts.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_string_counts

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_and_sort_strings(sample_strings))