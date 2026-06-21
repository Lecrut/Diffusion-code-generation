items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search(item):
    return item in items

def filter_items(predicate):
    return tuple(filter(predicate, items))

def sort_items(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))
if __name__ == '__main__':
    print(search('banana'))
    print(search('grape'))
    print(filter_items(lambda x: len(x) > 5))
    print(sort_items(key=len))
    print(sort_items(key=lambda x: x[0], reverse=True))