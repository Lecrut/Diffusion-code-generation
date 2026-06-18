import sys
def remove_duplicates(arr):
    if not isinstance(arr, (list, tuple)):
        raise TypeError(f"Expected 'list' or 'tuple', got {type(arr).__name__}")
    seen = {}
    result_list = []
    for item in arr:
        if item not in seen:
            seen[item] = True                                                
            result_list.append(item)
    return result_list
if __name__ == '__main__':
    sample_input = [3, 5, 2, 10, 8, 4, 6, 7, 9]
    try:
        unique_elements = remove_duplicates(sample_input)
        print(unique_elements)
    except TypeError as e:
        print(f"Error processing input: {e}", file=sys.stderr)