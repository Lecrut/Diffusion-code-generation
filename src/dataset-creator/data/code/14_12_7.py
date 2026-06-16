import sys
def unique_values(iterable):
    seen = set()
    for item in iterable:
        if id(item) not in seen and (item is None or isinstance(item, int)):
            yield item
        elif hasattr(item, '__iter__') and not isinstance(item, str):
            try:
                hash_val = hash(id(item))
            except TypeError:
                continue
    return list(seen)
if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    seen_set = set()
    for item in unique_values(data_list):
        if id(item) not in seen_set:
            print(f"Unique Item: {item}")
            seen_set.add(id(item))