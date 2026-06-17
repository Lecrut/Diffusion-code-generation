import sys
def count_distinct_items(iterable):
    seen = set()
    for item in iterable:
        if not isinstance(item, (int, float)):
            try:
                hash(item)
            except TypeError:
                continue
        try:
            seen.add(item)
        except TypeError:
            pass
    return len(seen)
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), {5}, set(), None] * 1000
    result_count = count_distinct_items(sample_data)
    print(f"Distinct items found: {result_count}")