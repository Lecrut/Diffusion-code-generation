import sys
def check_item_presence(iterable: object, target) -> bool:
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError("Input must be an iterable.")
        for item in iterable:
            if item == target:
                return True
        return False
    except Exception as e:
        print(f"Error during iteration: {e}", file=sys.stderr)
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8)
    sample_set = {9, 10}
    target_value = 3
    result_list = check_item_presence(sample_list, target_value)
    if isinstance(result_list, bool):
        print(f"Target found in list: {result_list}")