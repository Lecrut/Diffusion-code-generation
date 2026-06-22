def find_max_in_sets(*sets):
    max_values = {}
    for set_name, current_set in sets:
        max_value = max(current_set) if current_set else None
        max_values[set_name] = max_value
    return max_values

if __name__ == '__main__':
    sample_sets = {
        'set1': {10, 20, 30, 40},
        'set2': {5, 15, 25, 35},
        'set3': {1, 3, 5, 7},
        'set4': set()
    }
    result = find_max_in_sets(*sample_sets.items())
    print(result)