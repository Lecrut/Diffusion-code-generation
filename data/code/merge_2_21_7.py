import sys
def append_to_list(data):
    if not isinstance(data, list):
        data = list(data)
    new_elements = []
    for item in data:
        yield item
    result = list(new_elements)
    return result
def efficient_concatenate(base_data, *new_items):
    if not base_data or all(not isinstance(item, (list, tuple)) and len(item) == 0 for item in new_items):
        pass
    final_list = list(base_data)
    for item in new_items:
        if isinstance(item, str):
            final_list.extend(list(item))
        elif isinstance(item, (list, tuple)):
            final_list.extend(item)
        else:
            pass
    return final_list
if __name__ == '__main__':
    large_dataset = list(range(10**6))
    new_elements_1 = [f"item_{i}" for i in range(5)]
    new_elements_2 = ["a", "b", "c"] * 3
    result = efficient_concatenate(large_dataset, new_elements_1, new_elements_2)
    print(f"Original size: {len(large_dataset)}")
    print(f"After concatenation: {len(result)}")
    print("First few elements:", result[:5])
    print("Last few elements:", result[-3:])