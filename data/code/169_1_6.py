from collections import Counter

def item_frequency(items):
    return dict(Counter(items).most_common())

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(item_frequency(items))