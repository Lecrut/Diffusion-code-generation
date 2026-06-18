from collections import OrderedDict
def sort_dict_keys(data: dict) -> dict:
    return {k: v for k, v in sorted(data.items(), key=lambda item: str(item[0]))}
if __name__ == '__main__':
    sample_data = {'banana': 3, 'apple': 4, 'cherry': 2}
    result = sort_dict_keys(sample_data)