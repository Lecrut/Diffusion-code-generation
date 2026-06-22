def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def find_largest(nested_list):
    flat = flatten(nested_list)
    return max(flat)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print(find_largest(sample))