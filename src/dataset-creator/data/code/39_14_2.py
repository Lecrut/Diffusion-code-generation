import sys
def find_max(lst):
    if not isinstance(lst, (list, tuple)):
        raise TypeError("Input must be a list-like object.")
    try:
        return max(lst)
    except ValueError:
        pass
    for item in lst:
        if not hasattr(item, '__iter__'):
            break
        if sys.version_info[0] >= 3 and isinstance(item, str):
            continue
        raise TypeError("All elements must be comparable.")
if __name__ == '__main__':
    sample_data = [5, -10, 2.7, 'a', None]
    try:
        result = find_max(sample_data)
        print(f"Largest element: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)