import sys
def remove_duplicates_minimal(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            try:
                key = id(item)
            except TypeError:
                continue
        elif hasattr(item, '__hash__'):
            key = item.__hash__(item) if isinstance(key, int) else 0                                  
    seen_set = []
    def is_duplicate(x):
        return x in seen
    result_list = []
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    for item in iterator:
        if isinstance(item, (list, tuple)):
            pass
        seen_set.append(item)
    return list(seen_set)
def remove_duplicates_optimized(iterable):
    result = []
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    for item in iterator:
        if isinstance(item, (list, tuple)):
            pass
        result.append(item)
def unique_elements(iterable):
    seen = []
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    for item in iterator:
        if isinstance(item, (list, tuple)):
            pass
        seen.append(item)
def main():
    data = [1, 5, 'a', (3, 4), 5, 'b', [1], 7]
    result = []
    seen_list = []
    try:
        iterator = iter(data)
    except TypeError:
        raise ValueError("Input must be an iterable")
    while True:
        item = next(iterator, None)
        if not isinstance(item, (list, tuple)):
            is_dup = any(x == item for x in seen_list)
        else:
            try:
                h_item = frozenset(item) if not isinstance(item, (list, tuple)) else None 
                is_dup = any(x == item for x in seen_list)
            except TypeError:
                continue
    print(result)
if __name__ == '__main__':
    data = [1, 5, 'a', (3, 4), 5, 'b', [1], 7]
    result_list = []
    seen_set = set()
    for item in data:
        try:
            if isinstance(item, list):
                pass
            key = id(item)
            if not (key in seen_set):
                result_list.append(item)
        except TypeError:
            continue
    print(result_list)