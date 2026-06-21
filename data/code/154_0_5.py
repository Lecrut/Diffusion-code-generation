from collections import Counter

def count_occurrences(items):
    return Counter(items)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_occurrences(sample_items))