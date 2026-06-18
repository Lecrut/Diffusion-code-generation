import sys
def remove_duplicates(arr):
    if not isinstance(arr, (list)):
        raise TypeError(f"Expected 'list' as first argument but got '{type(arr).__name__}'.")
    if len(arr) == 0:
        return []
    seen = set()
    result_list = list()
    for item in arr:
        if item not in seen:
            seen.add(item)
            result_list.append(item)
    return result_list
if __name__ == '__main__':
    sample_data = [1, 5, 2, 1, -9, 3, 3]
    try:
        unique_elements = remove_duplicates(sample_data)
        print(f"Input Array: {sample_data}")
        print(f"Unique Elements (Order Preserved): {unique_elements}")
    except TypeError as e:
        error_message = f"Error: Invalid Input Type - {str(e)}"
        sys.stderr.write(error_message + "\n")