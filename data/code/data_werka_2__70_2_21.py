def get_ends(iterable):
    it = iter(iterable)
    first = next(it)
    last = first
    for current in it:
        last = current
    return (first, last)

def safe_get_ends(iterable):
    try:
        return get_ends(iterable)
    except StopIteration:
        raise ValueError("iterable is empty")

if __name__ == '__main__':
    print(safe_get_ends([1, 2, 3, 4, 5]))
    try:
        print(safe_get_ends([]))
    except ValueError as e:
        print(e)
    print(safe_get_ends("python"))