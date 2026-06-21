items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search_item(item_name):
    return item_name in items

def filter_items(predicate):
    return tuple(filter(predicate, items))

def sort_items(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))
if __name__ == '__main__':
    print(search_item('banana'))
    print(search_item('grape'))
    print(filter_items(lambda x: len(x) > 5))
    print(sort_items(key=len))
    print(sort_items(reverse=True, key=len))