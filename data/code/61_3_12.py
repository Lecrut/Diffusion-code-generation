def fetch_element_by_index(data_list, index):
    return data_list[index]

if __name__ == '__main__':
    sample_values = {
        'list1': [5, 15, 25, 35, 45, 55],
        'list2': ['a', 'b', 'c', 'd', 'e', 'f']
    }
    print(fetch_element_by_index(sample_values['list1'], 4))