def check_target_presence(data_list, search_term):
    data_set = set(data_list)
    return search_term in data_set

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    target_item = 'banana'
    print(check_target_presence(sample_data, target_item))