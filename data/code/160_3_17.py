items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search_item(item_name):
    return item_name in items

def filter_items(filter_func):
    return tuple(filter(filter_func, items))

def sort_items(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))
if __name__ == '__main__':
    print(search_item('banana'))
    print(search_item('grape'))
    filtered = filter_items(lambda x: len(x) > 5)
    print(filtered)
    sorted_items = sort_items(key=len, reverse=True)
    print(sorted_items)