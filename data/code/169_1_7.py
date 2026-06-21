from collections import Counter

def count_items(item_list):
    return dict(Counter(item_list))

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    result = count_items(items)
    for item, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(f"{item}: {count}")