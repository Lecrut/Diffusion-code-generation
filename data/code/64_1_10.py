def find_final_index(data_list, target_item):
    return data_list[::-1].index(target_item) if target_item in data_list else -1

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'banana', 'elderberry']
    target = 'banana'
    result = find_final_index(sample_data, target)
    print(result)

    another_sample_data = [10, 20, 30, 40, 50]
    another_target = 30
    another_result = find_final_index(another_sample_data, another_target)
    print(another_result)

    no_match_data = [1, 2, 3, 4, 5]
    no_match_target = 6
    no_match_result = find_final_index(no_match_data, no_match_target)
    print(no_match_result)