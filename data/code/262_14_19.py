def find_min_max(data):
    if not data:
        return None, None
    first, *rest = data
    minimum = maximum = first
    for x in rest:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")