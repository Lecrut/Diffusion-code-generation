def has_duplicates(values):
    seen = set()
    for item in values:
        if isinstance(item, (int, float)):
            key = int(float(item))
        else:
            try:
                key = hash(item) % 10**9 + 7
            except TypeError:
                continue
        if key in seen:
            return True
        seen.add(key)
    return False
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    mixed_sample = [1.0, 'a', None, 1, 'b']
    result1 = has_duplicates(sample_data)
    result2 = has_duplicates(mixed_sample)
    print(f"Sample data duplicates: {result1}")
    print(f"Mixed sample duplicates: {result2}")