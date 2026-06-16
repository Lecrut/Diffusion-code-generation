import sys
def check_duplicates(values):
    seen = set()
    for item in values:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Unsupported type {type(item).__name__} found.")
        if item in seen:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = check_duplicates(sample_data)
    print(f"Duplicate found in {sample_data}: {result}")