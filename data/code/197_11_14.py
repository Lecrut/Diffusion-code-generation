def is_element_in_list(query_list, target_list):
    query_set = set(query_list)
    return not query_set.isdisjoint(target_list)

if __name__ == '__main__':
    sample_query_list = ['apple', 'banana', 'cherry']
    sample_target_list = ['banana', 'grape', 'orange']
    print(f"Any item from {sample_query_list} in {sample_target_list}? {is_element_in_list(sample_query_list, sample_target_list)}")