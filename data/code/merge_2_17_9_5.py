import sys
def exists_optimized(items: list, target) -> bool:
    seen = set()
    for item in items:
        if item == target:
            return True
        elif isinstance(item, (list, dict)):
            try:
                hashable_item = tuple(sorted((type(item).__name__, str(item))))
            except TypeError:
                continue
            else:
                seen.add(hashable_item)
    for key in seen:
        if target == list(key)[0]:
            return True
    return False
if __name__ == '__main__':
    data = [1, 2, 'a', {'x': 1}, ['b'], 3]
    print(exists_optimized(data, 2))