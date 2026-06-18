import re
def normalize_name(name: str) -> str:
    return name.strip().lower()
def get_unique_animals(*names):
    normalized_list = [normalize_name(n) for n in names]
    unique_set = set(normalized_list)
    sorted_result = sorted(unique_set, key=lambda x: re.sub(r'[^a-z]', '', x))
    return list(sorted_result)
if __name__ == '__main__':
    sample_data_1 = ['Lion', 'Tiger', 'LEOPARD']
    sample_data_2 = {'Wolf', 'wolf', 'WOLF'}
    all_names = *sample_data_1, *list(sample_data_2)
    result = get_unique_animals(*all_names)
    print(result)