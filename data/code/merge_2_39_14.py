import sys
def find_max(data):
    try:
        if not data:
            raise ValueError("Input list is empty")
        max_val = -sys.maxsize
        for item in data:
            if isinstance(item, (int, float)):
                if item > max_val:
                    max_val = item
            else:
                try:
                    num_item = int(float(item))
                    if num_item > max_val:
                        max_val = num_item
                except ValueError:
                    raise TypeError(f"Unsupported element type in list: {type(item)}")
        return max_val
    except Exception as e:
        print(f"Error finding maximum value: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [3, 5.2, -10, "4", True]
    try:
        result = find_max(sample_list)
        print(f"Largest element is: {result}")
    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)