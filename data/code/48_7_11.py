def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def max_from_nested(nested):
    flat = flatten(nested)
    return max(flat)

if __name__ == '__main__':
    sample_data = [[1, 2, [3, 4]], [5, [6, 7]], 8, [9, [10]]]
    print(max_from_nested(sample_data))