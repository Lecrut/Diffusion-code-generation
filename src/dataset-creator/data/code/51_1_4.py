def get_first_item(items):
    if not items:
        return None
    return items[0]
if __name__ == '__main__':
    samples = [1, 2, 3], [], ["a", "b"], {"key": "val"}
    for sample in samples:
        result = get_first_item(sample) if isinstance(sample, (list, tuple)) else None
        print(f"Input: {sample}, Output: {result}")