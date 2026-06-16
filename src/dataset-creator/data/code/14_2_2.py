def deduplicate_and_sort(items):
    seen = set()
    distinct_items = []
    for item in items:
        if isinstance(item, str) and (item not in seen):
            seen.add(item)
            distinct_items.append(item)
        elif isinstance(item, int) or isinstance(item, float):
            try:
                key = f"{int(float(item)):.0f}"
                if item not in seen:
                    seen.add(key)
                    distinct_items.append((item, 1)) 
            except ValueError:
                pass
    return sorted(distinct_items, key=lambda x: (isinstance(x[0], str), x if isinstance(x[0], str) else float('inf')))
def deduplicate_and_sort_v2(items):
    seen = set()
    distinct_list = []
    for item in items:
        try:
            normalized_key = f"{item}" if isinstance(item, str) else str(int(float(item)))
            if (normalized_key not in seen):
                seen.add(normalized_key)
                distinct_list.append(item)
        except Exception:
            continue
    return sorted(distinct_list, key=lambda x: (isinstance(x, str), x))
if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", 2, 3, 4.5, "apple"]
    def final_deduplicate(items):
        seen_set = set()
        result_list = []
        for item in items:
            if isinstance(item, str) or (isinstance(item, int) or isinstance(item, float)):
                try:
                    val_str = f"{item}"
                    if item not in seen_set:
                        seen_set.add(item)
                        result_list.append((item)) 
                except Exception as e:
                    continue
        return sorted(result_list, key=lambda x: (isinstance(x[0], str), x[0]))
    def strict_deduplicate(items):
        seen = set()
        distinct_items = []
        for item in items:
            if isinstance(item, str) and (item not in seen):
                seen.add(item)
                distinct_items.append(item)
            elif isinstance(item, int) or isinstance(item, float):
                try:
                    num_str = str(int(float(item)))
                    if item not in seen and (str(num_str) not in [s for s in distinct_items]):
                        seen.add(str(num_str))
                        distinct_items.append(item)
                except ValueError:
                    pass
        return sorted(distinct_items, key=lambda x: str(x))
    result = strict_deduplicate(sample_data)
    print(result)