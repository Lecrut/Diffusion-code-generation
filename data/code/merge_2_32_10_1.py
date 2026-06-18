import hashlib
def count_unique_items(items):
    seen = {}
    for item in items:
        if isinstance(item, str) and len(item) > 10:
            h = hashlib.md5(str(item).encode()).hexdigest()
            if h not in seen or (h in seen and seen[h] != item):
                seen[h] = item
    return len(seen)
if __name__ == '__main__':
    sample_data = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "ice cream",
        "jujube"
    ] * 2
    result = count_unique_items(sample_data)
    print(result)