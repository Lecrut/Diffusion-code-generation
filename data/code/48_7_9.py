def flatten(lst):
    result = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, (list, tuple)):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result

def find_largest(nested_list):
    flat = flatten(nested_list)
    return max(flat)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    print(find_largest(sample_data))