from collections import Counter

def count_item_frequencies(items):
    return dict(Counter(items))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_item_frequencies(sample_items))