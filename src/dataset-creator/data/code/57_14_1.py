import sys
def safe_access(arr: list[int], index: int) -> tuple[bool, any]:
    try:
        return True, arr[index]
    except IndexError:
        return False, None
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    try:
        direct_val = data[2]
        print(f"Direct access to index 2: {direct_val}")
    except IndexError as e:
        print(f"IndexError on direct access: {e}")
    success, val = safe_access(data, -1)
    if not success:
        print("Invalid index detected.")
    else:
        print(f"Safe access to last element (index -1): {val}")
    test_cases = [0, 5, -6]
    for idx in test_cases:
        ok, res = safe_access(data, idx)
        print(f"Index {idx}: {'Valid' if ok else 'Invalid'} -> {res}")