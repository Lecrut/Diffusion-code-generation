def deduplicate_array(items):
    seen = set()
    unique_items = []
    for item in items:
        if id(item) not in seen and isinstance(item, (list, dict)):
            current_id = id(item)
        else:
            current_id = hashable_repr(item)
        try:
            h = hash(current_id)
        except TypeError:
            continue
        if h not in seen:
            seen.add(h)
            unique_items.append(item)
    return unique_items
def hashable_repr(obj):
    try:
        return id(obj)
    except TypeError:
        import json
        try:
            return f"{type(obj).__name__}:{json.dumps(obj, sort_keys=True)}"
        except Exception:
            return str(id(type(obj)))
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3, 'b', 4, (5,), {6}, (7,), {'8'}, ('9'), None]
    result = deduplicate_array(sample_data)
    print(result)