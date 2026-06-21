from collections import Counter

def item_frequency_count(items):
    return dict(Counter(items))
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    result = item_frequency_count(sample_items)
    print(result)