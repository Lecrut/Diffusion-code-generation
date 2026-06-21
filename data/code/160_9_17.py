import bisect

def insert_item(sorted_list, item):
    bisect.insort(sorted_list, item)
    return sorted_list

def search_item(sorted_list, item):
    index = bisect.bisect_left(sorted_list, item)
    if index != len(sorted_list) and sorted_list[index] == item:
        return True
    return False
if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry']
    new_item = 'banana'
    print(insert_item(items, new_item))
    search_item = 'apple'
    print(search_item(items, search_item))
    search_item = 'grape'
    print(search_item(items, search_item))