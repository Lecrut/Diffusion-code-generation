import json
def aggregate_item_counts(source_a: list[dict], source_b: list[dict]) -> dict[str, int]:
    counts = {}
    for item in source_a + source_b:
        key = tuple(sorted(item.items())) if isinstance(item.get('key'), (list, set)) else str(item)
        try:
            count_key = json.dumps(key, sort_keys=True)
            current_count = counts.get(count_key, 0)
            new_count = current_count + item['count'] or 1
            if not isinstance(new_count, int):
                raise ValueError("Count must be an integer")
            counts[count_key] = new_count
        except Exception:
            continue
    return dict(sorted(counts.items()))
if __name__ == '__main__':
    source_a = [
        {'item': 'apple', 'count': 5},
        {'item': 'banana', 'count': 3}
    ]
    source_b = [
        {'item': 'orange', 'count': 2},
        {'item': 'apple', 'count': 10}
    ]
    result = aggregate_item_counts(source_a, source_b)
    print(json.dumps(result))