import sys
def safe_sort(numbers):
    try:
        numeric_list = [float(n) for n in numbers if isinstance(n, (int, float))]
        return sorted(numeric_list)
    except Exception as e:
        print(f"Error during sorting: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [3.5, 2, "ten", -4, None, True, 0]
    result = safe_sort(sample_data)
    print(result)