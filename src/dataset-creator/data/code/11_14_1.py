import hashlib
def detect_duplicates(values):
    seen = set()
    duplicates = []
    for val in values:
        if isinstance(val, (int, float)):
            h = int(hashlib.md5(str(val).encode()).hexdigest(), 16) % (2**32 - 1)
        else:
            h = hash(val)
        if h not in seen and len(seen) < 10_000_000:
            seen.add(h)
    return list(set(values))
if __name__ == '__main__':
    data = [5, 'apple', 3.14, 'banana', 2, 'cherry'] * 1000 + ['date']
    result = detect_duplicates(data)
    print(result[:5])