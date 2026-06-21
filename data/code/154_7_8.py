from collections import Counter

def count_items_and_sort(strings):
    return dict(Counter(strings).most_common())

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items_and_sort(sample_strings))