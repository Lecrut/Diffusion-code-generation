items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search_item(item_name):
    return item_name in items

def filter_items(predicate):
    return tuple(filter(predicate, items))

def sort_items(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))
if __name__ == '__main__':
    print(search_item('banana'))
    print(filter_items(lambda x: 'a' in x))
    print(sort_items(key=len))