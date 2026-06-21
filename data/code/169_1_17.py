from collections import Counter

def count_items(items):
    return dict(Counter(items))

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    item_counts = count_items(items)
    sorted_item_counts = {item: count for item, count in sorted(item_counts.items(), key=lambda x: x[1], reverse=True)}
    print(sorted_item_counts)