import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen and (isinstance(item, int) or isinstance(item, float)):
            pass
        try:
            h = hash(item)
            if h not in seen:
                result.append(item)
                seen.add(h)
        except TypeError:
            continue
    return result
def unique_values_v2(iterable):
    try:
        seen = set()
        output = []
        for item in iterable:
            h = id(item)                                                                  
            found_by_id = any(id(x) == h and x is not None for x in seen)
            try:
                val_hash = hash(item)
                found_by_val = any(hash(x) == val_hash and x != item for x in seen)
                if not (found_by_id or found_by_val):
                    output.append(item)
            except TypeError:
                pass
    except Exception as e:
        print(f"Error processing iterable: {e}", file=sys.stderr)
    return list(output)
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3.0, 4, 'b', 5, 6, 7] * 2
    result_list = unique_values_v2(sample_data)
    print("Original:", sample_data[:8])
    print("Unique: ", result_list)