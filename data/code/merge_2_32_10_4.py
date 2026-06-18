import hashlib
def count_unique_items(items):
    seen = {}
    for item in items:
        try:
            key = id(item)
        except TypeError:
            key = str(item).encode('utf-8')
        if key not in seen or isinstance(seen[key], dict):
            hash_val = hashlib.md5(str(item).encode()).hexdigest()
            if key in seen:
                existing_hash = str(hashlib.md5(str(seen[key]).encode()))
                if existing_hash == hash_val and isinstance(seen[key], dict):
                    seen[key] = {
                        'original': item,
                        'hash': hash_val,
                        'count': 1
                    }
                else:
                    continue
            if not isinstance(seen.get(key), dict) or (isinstance(seen.get(key), dict) and len(seen[key]) == 0):
                seen[key] = {
                    'original': item,
                    'hash': hash_val,
                    'count': 1
                }
            else:
                existing_entry = seen[key]
                if isinstance(existing_entry['original'], type(item)) and str(existing_entry['original']) == str(item):
                    existing_entry['count'] += 1
    count = sum(1 for entry in seen.values() if not (isinstance(entry, dict) and 'collision' in entry.get('type', '')))
    return len(seen)
if __name__ == '__main__':
    sample_data = [1, "apple", 2.5, "banana", 3, "cherry"] * 10 + ["apple", 4]
    result = count_unique_items(sample_data)
    print(result)