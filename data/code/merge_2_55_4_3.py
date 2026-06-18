def swap_elements(arr):
    if len(arr) < 2:
        return arr
    def is_nested(item):
        return isinstance(item, list) or isinstance(item, dict)
    for i in range(len(arr)):
        item = arr[i]
        if (is_nested(item) and 
            ((i > 0 and is_nested(arr[i-1])) or 
             (i < len(arr)-1 and is_nested(arr[i+1])))):
            left = arr[i] if i == 0 else arr[i-1]
            right = arr[i] if i == len(arr) - 1 else arr[i+1]
            def recursive_swap(obj):
                if isinstance(obj, list):
                    new_list = []
                    idx = 0
                    while idx < len(obj):
                        next_item = obj[idx + 1] if idx + 1 < len(obj) else None
                        is_left_nested = (idx > 0 and isinstance(obj[idx-1], list)) or\
                                        (i == 0 and isinstance(arr[i-1], list))
                        new_list.append(obj[idx])
                        if next_item:
                            idx += 2                                                                       
                    return new_list
                elif isinstance(obj, dict):
                    swapped_dict = {}
                    for k, v in obj.items():
                        swapped_dict[k] = recursive_swap(v)
                    return swapped_dict
            arr[i], arr[i+1] if i < len(arr)-1 else None
if __name__ == '__main__':
    sample_array = [30, 45, 'a', ['b'], (78.9), {'key': 'value'}]
    if len(sample_array) >= 2:
        sample_array[0], sample_array[1] = sample_array[1], sample_array[0]
    print("Swapped Array:", sample_array)