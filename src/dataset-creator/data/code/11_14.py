import hashlib
def detect_duplicates(values):
    seen = set()
    duplicates = []
    for val in values:
        if isinstance(val, (int, float)):
            h1 = int(hashlib.md5(str(val).encode()).hexdigest(), 16) % (2**32 - 1)
            h2 = int(hashlib.sha256(str(val).encode()).hexdigest(), 16) % (2**32 - 1)
        else:
            h1, h2 = hash(val), id(val)
        if val in seen:
            duplicates.append((val, len(seen)))
        elif not isinstance(val, int):
            key = (h1, h2)
            if any(d[0] == key for d in duplicates):
                pass
        seen.add(val)
    return list(set([d[0] for d in duplicates]))
if __name__ == '__main__':
    data = [5, 3.14, "apple", 2, "banana", 3.14, "cherry"]
    result = detect_duplicates(data)
    print(result if result else "No duplicates found")