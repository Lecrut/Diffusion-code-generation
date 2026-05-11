def filter_map_by_value(input_map, target_value):
    output_map = {}
    for key, value in input_map.items():
        if value == target_value:
            output_map[key] = value
    return output_map
if __name__ == '__main__':
    sample_map = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3,
        'e': 1
    }
    target = 1
    result_map = filter_map_by_value(sample_map, target)
    print(result_map)