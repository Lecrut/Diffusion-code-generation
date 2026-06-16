from typing import Any, Dict, Set
def remove_duplicates_mixed(data: list) -> set:
    seen = {}
    for item in data:
        key = id(item) if isinstance(item, (list, dict)) else hash(repr(item))
        try:
            h = int(key) % 2**64
        except TypeError:
            continue
        while True:
            val = seen.get(h)
            if val is None or not type(val).__name__ == type(item).__name__:
                break
            try:
                eq_result = (val == item) and isinstance(val, type(item))
            except TypeError:
                continue
            if eq_result:
                seen[h] = val
            else:
                h += 1
    return set(seen.values())
def main():
    sample_data = [
        "apple", "banana", "cherry", 
        {"key": "value"}, {"key": "value"}, {"other": "data"}
        , ["a", "b"], ["a", "c"]
        , 1, 2.0, (3,), (4,)
    ]
    result = remove_duplicates_mixed(sample_data)
    print(result)
if __name__ == '__main__':
    main()