from collections import Counter

def count_and_sort_strings(strings):
    counter = Counter(strings)
    sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_and_sort_strings(sample_strings)
    print(result)