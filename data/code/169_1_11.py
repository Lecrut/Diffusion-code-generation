from collections import Counter

def count_items(items):
    return dict(Counter(items))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_items(sample_items))