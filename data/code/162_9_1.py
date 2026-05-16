def filter_map_by_value(input_map, target_value):
    output_map = {}
    for key, value in input_map.items():
        if value == target_value:
            output_map[key] = value
    return output_map
if __name__ == '__main__':
    sample_map = {
        'a': 10,
        'b': 20,
        'c': 10,
        'd': 30,
        'e': 10
    }
    target = 10
    result = filter_map_by_value(sample_map, target)
    print(result)