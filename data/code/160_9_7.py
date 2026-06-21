import bisect

def insert_sorted(items, item):
    bisect.insort(items, item)
    return items

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    new_item = 'date'
    sorted_items = insert_sorted(sample_items, new_item)
    print(sorted_items)