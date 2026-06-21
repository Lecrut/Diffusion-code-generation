from collections import Counter

def count_items(items):
    return dict(Counter(items))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    item_count = count_items(sample_items)
    sorted_item_count = {k: v for k, v in sorted(item_count.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_item_count)