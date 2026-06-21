items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search_item(query):
    return [item for item in items if query.lower() in item.lower()]

def filter_items(predicate):
    return tuple(filter(predicate, items))

def sort_items(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))

if __name__ == '__main__':
    print(search_item('an'))
    print(filter_items(lambda x: len(x) > 5))
    print(sort_items(key=len))