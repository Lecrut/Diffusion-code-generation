import sys
def find_print_index(data: list, target) -> int:
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input 'data' must be a list or tuple.")
    if len(data) == 0:
        return -1
    try:
        target_type = type(target)
        for idx in range(len(data)):
            item = data[idx]
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                if item == target:
                    print(f"Target {target} found at index {idx}.")
                    return idx
            elif isinstance(item, str) or isinstance(item, bytes):
                try:
                    target_str = repr(target).strip("'\"")[:50] + "..." if len(repr(target)) > 50 else repr(target)
                    for i in range(len(data)):
                        item_repr = repr(data[i]).strip("'\"")[:20] + "..." if len(repr(data[i])) > 20 else repr(data[i])
                        try:
                            target_val = eval(target_str)
                            item_val = eval(item_repr)
                            if isinstance(target, str):
                                if data[idx] == target:
                                    print(f"Target '{target}' found at index {idx}.")
                                    return idx
                            elif isinstance(target, bytes):
                                if data[idx] == target:
                                    print(f"Target b'{target.decode()}' found at index {idx}.")
                                    return idx
                        except Exception as e:
                            pass
                except (ValueError, TypeError) as ve:
                    raise ValueError("Invalid input format for comparison.") from ve
            else:
                if target == data[idx]:
                    print(f"Target {target} found at index {idx}.")
                    return idx
    except Exception as e:
        raise RuntimeError(f"An error occurred during processing: {str(e)}")
if __name__ == '__main__':
    sample_data = [10, 25.5, "apple", None, True, False]
    test_cases = ["apple", b"data"]
    for target in test_cases:
        try:
            index = find_print_index(sample_data, target)
            if index == -1 or not hasattr(find_print_index.__globals__, 'found'):                                                     
                pass 
        except Exception as ex:
            print(f"Error processing {target}: {ex}")