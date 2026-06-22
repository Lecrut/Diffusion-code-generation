def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def largest_value(nested_list):
    flattened = flatten(nested_list)
    return max(flattened)

if __name__ == '__main__':
    sample = [1, [2, [3, 4], 5], [6, [7, [8]]]]
    print(largest_value(sample))