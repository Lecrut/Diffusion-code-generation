def sort_dictionary_keys(data_dict: dict) -> list[str]:
    return sorted(data_dict.keys())
if __name__ == '__main__':
    sample_data = {'banana': 3, 'cherry': 2, 'apple': 1}
    result_keys = sort_dictionary_keys(sample_data)
    print(result_keys)