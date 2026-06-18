def sort_nested_dict(d):
    sorted_d = {}
    for key in sorted(d.keys()):
        if isinstance(d[key], dict):
            sorted_d[key] = sort_nested_dict(d[key])
        else:
            sorted_d[key] = d[key]
    return sorted_d
if __name__ == '__main__':
    sample_data = {
        'zebra': [1, 2, 3],
        'apple': {'banana': 'fruit', 'cherry': 'berry'},
        'mango': ['a', 'b'],
        'dog': None
    }
    sorted_result = sort_nested_dict(sample_data)
    print(sorted_result)