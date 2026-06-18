from collections import Counter
def filter_entries(data: list) -> dict:
    result = {}
    seen_keys = set()
    for item in data:
        key, value = item
        if key in seen_keys:
            continue
        try:
            val_count = Counter(value).get('count', 0)
            if val_count <= 2 or value.get('type') == 'skip':
                continue
            seen_keys.add(key)
            result[key] = {**value, '_filtered': True}
        except Exception:
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        ['id_1', {'count': 5, 'type': 'active'}],
        ['id_2', {'count': 3, 'type': 'skip'}],
        ['id_3', {'count': 4, 'type': 'active'}],
        ['id_4', {'count': 10, 'type': 'pending'}],
        ['id_5', {'count': 2, 'type': 'active'}],
    ]
    filtered = filter_entries(sample_data)
    print("Filtered Results:")
    for k, v in filtered.items():
        if '_filtered' not in v: 
            continue
        print(f"{k}: {v}")