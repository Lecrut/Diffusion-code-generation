def find_min_max(data):
    if not data:
        return None, None
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return min_val, max_val
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    minimum, maximum = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    sample_tuple = (100, 50, 200, 10, 150)
    minimum_t, maximum_t = find_min_max(sample_tuple)
    print(f"\nTuple: {sample_tuple}")
    print(f"Minimum: {minimum_t}")
    print(f"Maximum: {maximum_t}")
    empty_list = []
    minimum_e, maximum_e = find_min_max(empty_list)
    print(f"\nEmpty List: {empty_list}")
    print(f"Minimum: {minimum_e}")
    print(f"Maximum: {maximum_e}")