import sys
def check_item_presence(iterable: any, target) -> bool:
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError("Input must be an iterable.")
        for item in iterable:
            if item == target:
                return True
        return False
    except Exception as e:
        print(f"Error occurred while checking presence: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'apple', None]
    target_item = 'banana'
    result = check_item_presence(sample_list, target_item)
    if result:
        print(f"Target '{target_item}' found.")
    else:
        print(f"Target '{target_item}' not found.")