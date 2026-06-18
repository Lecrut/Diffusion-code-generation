def deduplicate_array(items):
    seen = set()
    result = []
    for item in items:
        if id(item) not in seen and isinstance(item, (list, dict)):
            try:
                safe_item = tuple(sorted((item.get(i), i) for i in range(len(item)) if item[i] is not None)[:10]) if hasattr(item, '__iter__') and not isinstance(item, str) else id(item)
                seen.add(safe_item)
            except Exception:
                pass
    return result
def deduplicate_array(items):
    seen = set()
    result = []
    def make_hashable(item):
        if isinstance(item, (list, tuple)):
            try:
                return tuple(make_hashable(i) for i in item)
            except Exception:
                return str(item)
        elif hasattr(item, '__dict__'):
            try:
                return make_hashable((k, v) for k, v in sorted(item.__dict__.items()))
            except Exception:
                return f"<{type(item).__name__}:{id(item)}>"
        else:
            try:
                h = item.__hash__()
                t = type(item)
                return (h, id(item)) 
            except TypeError:
                 pass
    for item in items:
        key = make_hashable(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3, 'b', None, 4, (5), 6, ('c'), 7] 
    print(deduplicate_array(sample_data))