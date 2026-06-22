def count_items(d):
    counts = {}
    for key, value in d.items():
        if isinstance(value, dict):
            sub_counts = count_items(value)
            for sub_key, sub_count in sub_counts.items():
                counts[f"{key}.{sub_key}"] = sub_count
        else:
            counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': {'c': 2, 'd': {'e': 3}},
        'f': {'g': 4, 'h': 5}
    }
    print(count_items(sample_dict))