UNIQUE_ITEM_THRESHOLD = 1

def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if items.count(item) == UNIQUE_ITEM_THRESHOLD:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(unique_items(sample_items))