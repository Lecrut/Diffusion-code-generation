def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def largest_value(nested):
    flat_list = flatten(nested)
    return max(flat_list)

if __name__ == '__main__':
    data = [1, [2, 3], [4, [5, [6]]]]
    print(largest_value(data))