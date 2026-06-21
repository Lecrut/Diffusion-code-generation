import bisect

def insert_sorted(items, item):
    bisect.insort(items, item)
    return items

def binary_search(items, item):
    index = bisect.bisect_left(items, item)
    if index != len(items) and items[index] == item:
        return index
    return -1
if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry']
    new_item = 'banana'
    print(insert_sorted(items, new_item))
    search_item = 'banana'
    print(binary_search(items, search_item))
    search_item = 'grape'
    print(binary_search(items, search_item))