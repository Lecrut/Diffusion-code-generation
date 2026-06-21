sample_list_mapping = {
    'list1': [1, 2, 3],
    'list2': [4, 5, 6]
}

def combine_lists(list_key1, list_key2):
    result = sample_list_mapping[list_key1].copy()
    result.extend(sample_list_mapping[list_key2])
    return result

if __name__ == '__main__':
    combined_list = combine_lists('list1', 'list2')
    print(combined_list)