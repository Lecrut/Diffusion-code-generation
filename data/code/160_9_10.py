import bisect

def insert_sorted(item_list, item):
    bisect.insort(item_list, item)

def binary_search(item_list, item):
    index = bisect.bisect_left(item_list, item)
    if index != len(item_list) and item_list[index] == item:
        return index
    else:
        return -1

if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry']
    insert_sorted(items, 'date')
    print("Sorted list:", items)
    
    search_item = 'banana'
    result = binary_search(items, search_item)
    if result != -1:
        print(f"'{search_item}' found at index {result}")
    else:
        print(f"'{search_item}' not found")