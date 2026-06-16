import sys
def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        try:
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError as e:
            raise TypeError(f"Input contains non-hashable elements. Error details: {e}")
    return result
if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5]
    try:
        unique_elements = remove_duplicates(input_array)
        if not isinstance(unique_elements, list):
            raise TypeError("Function did not return a list.")
        print(f"Input Array: {input_array}")
        print(f"Unique Elements (Order Preserved): {unique_elements}")
    except Exception as e:
        error_message = f"An error occurred during processing: {e}"
        sys.stderr.write(error_message + "\n")