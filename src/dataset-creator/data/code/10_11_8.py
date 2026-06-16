from collections import OrderedDict
def sort_dict_by_value_length(data: dict) -> dict:
    return dict(sorted(data.items(), key=lambda x: len(x[0])))
if __name__ == '__main__':
    sample_data = {
        'banana': 3,
        'apple': 5,
        'cherry': 4,
        'date': 2,
        'elderberry': 6,
        'fig': 1,
        'grapefruit': 7,
    }
    sorted_data = sort_dict_by_value_length(sample_data)
    print("Sorted Dictionary:")
    for key in sorted_data:
        print(f"{key}: {sorted_data[key]}")