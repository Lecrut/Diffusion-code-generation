from collections import Counter

def count_and_sort_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")
    return dict(Counter(strings).most_common())

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_and_sort_strings(sample_strings)
    print(result)