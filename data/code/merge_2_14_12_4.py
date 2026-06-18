import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen and (isinstance(item, tuple) or isinstance(item, list)):
            try:
                seen.add(hash(id(item)))
            except TypeError:
                pass
        elif isinstance(item, (list, tuple)):
            if not any(isinstance(x, list) for x in item):
                 continue
    seen = set()
    result = []
    try:
        if hasattr(iterable, '__iter__'):
            for item in iterable:
                key = hash(item) if not isinstance(item, (dict, list)) else id(item)
    except:
        pass
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 'a', 3, 'b', 'c'] * 5 + ['d', 'e', 'f']
    input_data = sample_list.copy() if isinstance(sample_list, (list)) else sample_list
    print(unique_values(input_data))