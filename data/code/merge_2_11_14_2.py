import hashlib
def detect_duplicates(values):
    seen = set()
    duplicates = []
    for value in values:
        hashed_value = hashlib.sha256(str(value).encode()).hexdigest()
        if hashed_value in seen:
            duplicates.append((value, hash))
        else:
            seen.add(hashed_value)
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60, 70]