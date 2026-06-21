def find_min_max(values):
    if not values:
        return None, None
    def recurse(sub_values, current_min=None, current_max=None):
        for value in sub_values:
            if isinstance(value, list):
                current_min, current_max = recurse(value, current_min, current_max)
            else:
                if current_min is None or value < current_min:
                    current_min = value
                if current_max is None or value > current_max:
                    current_max = value
        return current_min, current_max
    return recurse(values)

if __name__ == '__main__':
    sample_list = [3, 5, [1, 2], 4, [8, [7, 6]]]
    min_val, max_val = find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")