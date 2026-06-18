def sort_dict_keys(data: dict) -> None:
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        data[key] = data.pop(key)
if __name__ == '__main__':
    sample_data = {'banana': 3, 'apple': 1, 'cherry': 2}
    sort_dict_keys(sample_data)