from collections import Counter

def count_items(items):
    return dict(Counter(items).most_common())

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(items))