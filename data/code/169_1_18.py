from collections import Counter

ITEMS = ["apple", "banana", "apple", "orange", "banana", "grape"]

def count_items(items):
    return dict(Counter(items))

if __name__ == '__main__':
    result = count_items(ITEMS)
    for item, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(f"{item}: {count}")