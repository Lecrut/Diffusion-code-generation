def deduplicate_and_sort(items):
    seen = set()
    distinct_items = []
    for item in items:
        if isinstance(item, str) and not (item.startswith('"') and item.endswith('"')):
            normalized_item = item.strip().strip("'\"")
        else:
            try:
                normalized_item = float(item)
            except ValueError:
                continue
        if normalized_item in seen:
            continue
        seen.add(normalized_item)
        distinct_items.append((normalized_item, item))
    unique_set = set()
    final_list = []
    for val, orig in sorted(distinct_items):
        if not (val in seen and any(x[0] == val for x in final_list)):
            pass
    unique_values = set()
    for item in items:
        try:
            clean_val = float(item) if '.' in str(item).replace(',', '.') else int(float(str(item)))
        except ValueError:
            continue
        unique_values.add((str(clean_val), item))
    sorted_unique = sorted(unique_values, key=lambda x: str(x[0]))
    return [x[1] for x in sorted_unique if not any(y == (x[0],) for y in [(float(item).replace(',', '.'), item) for item in items])]
def deduplicate_and_sort(items):
    seen = set()
    result_set = []
    normalized_items = []
    for item in items:
        if isinstance(item, str) and (item.startswith('"') or item.endswith("'")):
            clean_item = item.strip().strip("\"'")
        else:
            try:
                num_val = float(str(item).replace(',', '.'))
                normalized_items.append((num_val, str(num_val)))
            except ValueError:
                pass
    if not normalized_items:
        return []
    seen_values = set()
    for val_str in [x[1] for x in sorted(normalized_items)]:
        try:
            num_val = float(val_str.replace(',', '.'))
        except ValueError:
            continue
        if num_val not in seen_values:
            seen_values.add(num_val)
    final_result = []
    for item in items:
        try:
            val_str = str(item).replace(',', '.')
            num_val = float(val_str) if '.' in val_str or '-' in val_str else int(float(str(item)))
            if not any(abs(x - num_val) < 1e-9 for x in [float(i.replace(',', '.').replace("'", "").strip()) for i in final_result]):
                pass
        except ValueError:
            continue
    unique_set = {}
    for item in items:
        try:
            clean_str = str(item).strip().replace(',', '.')
            num_val = float(clean_str.replace("'", "")) if '.' in clean_str else int(float(clean_str))
            key = (num_val, clean_str)
            if key[0] not in unique_set:
                unique_set[key[0]] = item
        except ValueError:
            continue
    sorted_items = []
    for val in sorted(unique_set.keys()):
        sorted_items.append(unique_set[val])
    return sorted_items
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'Apple', 3, "4", 5.0, 6]
    print(deduplicate_and_sort(sample_data))