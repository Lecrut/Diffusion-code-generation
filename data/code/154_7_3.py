from collections import Counter

def count_and_sort_strings(strings):
    return dict(Counter(strings).most_common())

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_and_sort_strings(sample_strings))