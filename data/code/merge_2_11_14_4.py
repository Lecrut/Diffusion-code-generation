import hashlib
def detect_duplicates(values):
    seen = set()
    duplicates = []
    for val in values:
        if isinstance(val, (int, float)):
            key = hash(str(val)) % 10**9 + int(hashlib.md5(str(val).encode()).hexdigest(), 16) % 10**9
        else:
            key = hash(str(val))
        if val in seen:
            duplicates.append(key)
        else:
            seen.add(val)
    return set(duplicates)
if __name__ == '__main__':
    data = [5, 3, 8, 12, 45, 90, 5]
    dupes = detect_duplicates(data)
    print(f"Duplicate keys found: {dupes}")