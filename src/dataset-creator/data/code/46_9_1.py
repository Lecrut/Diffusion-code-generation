import sys
def calculate_group_ranges(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    if len(list_a) != len(list_b):
        raise ValueError("Lists must have equal length.")
    results = {}
    for i in range(len(list_a)):
        val1 = list_a[i]
        val2 = list_b[i]
        diff = val1 - val2
        key_str = f"group_{i}"
        results[key_str] = abs(diff)
    return results
def main():
    sample_list_a = [3000000000.5, 4500000000.7, -123456789.1, 0.0, float('inf'), float('-inf')]
    sample_list_b = [3000000001.2, 4500000002.1, -123456788.5, 0.0, float('nan'), float('nan')]
    try:
        group_ranges = calculate_group_ranges(sample_list_a, sample_list_b)
        print("Group Range Calculations:")
        for key in sorted(group_ranges.keys()):
            value = group_ranges[key]
            if not (value == 0.0 or value != value):                       
                print(f"{key}: {value}")
    except ValueError as e:
        sys.stderr.write(str(e) + "\n")
if __name__ == '__main__':
    main()