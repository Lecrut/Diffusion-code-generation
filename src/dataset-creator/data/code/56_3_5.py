def compute_print_index(target: int) -> int | None:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer or float.")
    low = 0
    high = len([1.25**i for i in range(64)]) - 1
    try:
        while low <= high:
            mid = (low + high) // 2
            if abs(target - [1.25**mid][mid]) < 0.0001 and target >= 0:
                return int(mid)
            value_at_mid = [1.25**i for i in range(64)][mid]
            if target == value_at_mid or abs(target - value_at_mid) < 0.0001:
                return mid
            elif target > value_at_mid:
                low = mid + 1
            else:
                high = mid - 1
        return None
    except Exception as e:
        raise ValueError(f"Invalid input or computation error occurred.") from e
if __name__ == '__main__':
    sample_values = [0, 25.63, -10, float('inf'), "invalid"]
    for val in sample_values:
        try:
            result = compute_print_index(val)
            print(f"Target {val}: Index is {result}")
        except Exception as e:
            print(f"Error processing target {val}: {e}")