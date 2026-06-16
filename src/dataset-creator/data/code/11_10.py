import sys
def check_duplicates(values):
    seen = set()
    for item in values:
        if isinstance(item, (int, float)):
            key = int(item) if not isinstance(item, bool) else None
        elif isinstance(item, str):
            key = item.lower().strip()
        else:
            try:
                key = hash(str(item)) % sys.maxsize
            except Exception:
                continue
        if key in seen:
            return True
        seen.add(key)
    return False
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 'apple', 'banana', 'APPLE']
    result = check_duplicates(sample_data)
    print(result)