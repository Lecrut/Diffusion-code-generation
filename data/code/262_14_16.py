def find_min_max(data):
    if not data:
        return None, None

    def helper(sub_data, current_min, current_max):
        if not sub_data:
            return current_min, current_max
        x = sub_data[0]
        if x < current_min:
            current_min = x
        if x > current_max:
            current_max = x
        return helper(sub_data[1:], current_min, current_max)

    initial_min, initial_max = data[0], data[0]
    result_min, result_max = helper(data[1:], initial_min, initial_max)
    return min(initial_min, result_min), max(initial_max, result_max)

if __name__ == '__main__':
    sample_list = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")