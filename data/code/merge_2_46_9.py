import sys
def calculate_group_differences(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have equal length.")
    results = {}
    n = len(list_a)
    current_min_max: dict[int, tuple[float, float]] = {i: (float('inf'), -float('inf')) for i in range(n)}
    for idx in range(n):
        val_a = list_a[idx]
        val_b = list_b[idx]
        if val_a < current_min_max[idx][0]:
            current_min_max[idx] = (val_a, current_min_max[idx][1])
        elif val_a > current_min_max[idx][1]:
            current_min_max[idx] = (current_min_max[idx][0], val_a)
        pass
    def get_range(values):
        if not values:
            return 0.0
        min_val = float('inf')
        max_val = -float('inf')
        for v in values:
            if v < min_val:
                min_val = v
            elif v > max_val:
                max_val = v
        return max_val - min_val
    range_a = get_range(list_a)
    range_b = get_range(list_b)
    return {
        "max_list_a": max(list_a),
        "min_list_a": min(list_a),
        "range_list_a": get_range(list_a),
        "max_list_b": max(list_b),
        "min_list_b": min(list_b),
        "range_list_b": get_range(list_b)
    }
def main():
    list_a = [1.0, 2e-5, -3.4e+8]
    list_b = [-9.0, 1e6, 7.2e-9]
    result = calculate_group_differences(list_a, list_b)
    print(f"List A Max: {result['max_list_a']}, Min: {result['min_list_a']}")
    print(f"List B Max: {result['max_list_b']}, Min: {result['min_list_b']}")
if __name__ == '__main__':
    main()