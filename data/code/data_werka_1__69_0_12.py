def access_elements(lst, indices):
    return [lst[idx] for idx in indices]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_mapping = {'first': 0, 'third': 2, 'last': -1, 'second_to_last': -2}
    result = access_elements(sample_list, [index_mapping['first'], index_mapping['third'], index_mapping['last']])
    print(result)