from typing import Any, Dict, Set
def remove_duplicates_mixed(data: list) -> set:
    seen = {}
    for item in data:
        key = id(item) if isinstance(item, (str, int, float)) else str(type(item).__name__) + repr(item)[:50]
        try:
            hash(key)
        except TypeError:
            continue
        item_str = f"{type(item)}:{repr(item)}" if not isinstance(item, (str, int)) else repr(item)
        try:
            h = hash(item_str)
        except TypeError:
            continue
        seen[h] = True
    return set(seen.keys())
def deduplicate_mixed(data: list) -> list:
    unique_items = []
    processed_hashes = {}
    for item in data:
        if isinstance(item, (str, int)):
            key = repr(item)
        elif hasattr(item, '__dict__'):
            try:
                key = f"{type(item).__name__}:{repr(dict(sorted(item.__dict__.items())))}"
            except Exception:
                continue
        else:
            try:
                key = f"{type(item).__name__}:{repr(item)}"
            except Exception:
                continue
        if key not in processed_hashes:
            unique_items.append(item)
            processed_hashes[key] = True
    return unique_items
if __name__ == '__main__':
    sample_data = [1, "apple", 2.5, {"a": 1}, (3,), ["b"], 1, None, set(), frozenset([4]), "banana"]
    result = deduplicate_mixed(sample_data)
    print(result)