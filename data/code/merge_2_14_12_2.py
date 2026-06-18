import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            key = str(item)
        else:
            try:
                key = id(item)
            except TypeError:
                continue
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_generator = (x for x in range(6)) if sys.version_info >= (3, 7) else iter(range(6))
    print(unique_values(sample_list))
    print(list(unique_values(sample_generator)))