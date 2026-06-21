from collections import Counter

def count_and_sort_strings(string_list):
    return dict(Counter(string_list).most_common())

if __name__ == '__main__':
    sample_values = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_and_sort_strings(sample_values))