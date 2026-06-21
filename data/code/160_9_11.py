import bisect

def insert_sorted(items, item):
    bisect.insort(items, item)

def binary_search(items, item):
    index = bisect.bisect_left(items, item)
    if index != len(items) and items[index] == item:
        return index
    return -1
if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry']
    insert_sorted(items, 'date')
    print(items)
    search_item = 'banana'
    index = binary_search(items, search_item)
    print(index)