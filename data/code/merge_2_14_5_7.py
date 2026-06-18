def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            key = hash(tuple(sorted(item)))
        else:
            try:
                key = id(item)
            except TypeError:
                continue
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
def main():
    data = [1, 2, 'a', 3.5, (4, 5), 6, ('b', 'c'), 7]
    for item in remove_duplicates(data):
        print(item)
if __name__ == '__main__':
    main()