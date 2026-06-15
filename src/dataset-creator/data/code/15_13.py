def get_unique_sorted_items(input_string):
    if not isinstance(input_string, str):
        return []
    items = set(input_string)
    sorted_items = sorted(list(items))
    return sorted_items
if __name__ == '__main__':
    sample1 = "cbaabc"
    result1 = get_unique_sorted_items(sample1)
    print(f"Input: '{sample1}', Output: {result1}")
    sample2 = "programming"
    result2 = get_unique_sorted_items(sample2)
    print(f"Input: '{sample2}', Output: {result2}")
    sample3 = "hello world hello"
    result3 = get_unique_sorted_items(sample3)
    print(f"Input: '{sample3}', Output: {result3}")
    sample4 = 12345
    result4 = get_unique_sorted_items(sample4)
    print(f"Input: {sample4}, Output: {result4}")