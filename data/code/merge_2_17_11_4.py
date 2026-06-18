import sys
def check_item_presence(iterable: object, target) -> bool:
    try:
        if not isinstance(iterable, (list, tuple, set)):
            raise TypeError("Input must be a list, tuple, or set.")
        for item in iterable:
            if item == target:
                return True
        return False
    except Exception as e:
        print(f"Error during iteration: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [1, 2, 'apple', None]
    target_value = 'apple'
    result = check_item_presence(sample_list, target_value)
    if result:
        print(f"Target '{target_value}' found.")
    else:
        print(f"Target '{target_value}' not found.")