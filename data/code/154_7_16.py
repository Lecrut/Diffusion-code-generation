from collections import Counter

def count_items_and_sort(strings):
    counter = Counter(strings)
    sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_items_and_sort(sample_strings)
    print(result)