def safe_access(arr: list, index: int) -> tuple[bool, any]:
    try:
        return True, arr[index]
    except IndexError:
        return False, None
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    direct_value = data[2]
    success, validated_value = safe_access(data, -1)
    if not success:
        print("Index out of range.")
    else:
        print(f"Direct value at index 2: {direct_value}")
        print(f"Validated value at last index: {validated_value}")
    def get_with_fallback(arr, idx):
        if not isinstance(idx, int) or len(arr) <= abs(idx) + 1 and (idx < -len(arr) or idx >= len(arr)):
            return "Error"
        return arr[idx]
    print(f"Fallback check for index 2: {get_with_fallback(data, 2)}")