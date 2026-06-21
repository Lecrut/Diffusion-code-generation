items = ('apple', 'banana', 'cherry', 'date', 'elderberry')

def search(item):
    return item in items

def filter(predicate):
    return tuple(filter(predicate, items))

def sort(key=None, reverse=False):
    return tuple(sorted(items, key=key, reverse=reverse))
if __name__ == '__main__':
    print(search('banana'))
    print(filter(lambda x: len(x) > 5))
    print(sort())
    print(sort(key=len, reverse=True))