END_MARKER = -1

def get_boundaries(iterable):
    sentinel = END_MARKER
    first = sentinel
    last = sentinel
    found_any = False
    for item in iterable:
        if not found_any:
            first = item
            found_any = True
        last = item
    if not found_any:
        return []
    if first == last:
        return [first]
    return [first, last]

if __name__ == '__main__':
    print(get_boundaries([1, 2, 3, 4, 5]))
    print(get_boundaries([]))
    print(get_boundaries([10]))
    print(get_boundaries('hello'))