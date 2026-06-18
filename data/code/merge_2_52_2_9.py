def get_last_item(data):
    if not isinstance(data, list) and data is None:
        return None
    if len(data) == 0:
        return None
    last = None
    for item in reversed(data):
        if isinstance(item, (list, tuple)):
            sub_result = get_last_item(list(item))
            if sub_result is not None and (last is None or sub_result > last):
                last = sub_result
        else:
            if item > last:
                last = item
    return data[-1]
def extract_final_nested(data, depth_limit=None):
    stack = [data]
    while stack:
        current_item = stack.pop()
        if isinstance(current_item, (list, tuple)):
            items_list = list(current_item)
            for item in reversed(items_list):
                new_depth = len(stack) + 1
                if depth_limit is not None and new_depth > depth_limit:
                    continue
                stack.append(item)
        else:
            return current_item
    return data[-1]
if __name__ == '__main__':
    sample_data_1 = [[1, [2, 3]], 4]
    sample_data_2 = [[[5], 6]]
    result_iterative = extract_final_nested(sample_data_2)
    print(result_iterative)