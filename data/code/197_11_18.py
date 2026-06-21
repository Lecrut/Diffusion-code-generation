def check_element_presence(query_list, target_checklist):
    if not query_list or not target_checklist:
        return False
    query_set = set(query_list)
    target_set = set(target_checklist)
    return not query_set.isdisjoint(target_set)
if __name__ == '__main__':
    sample_query_list = ['apple', 'banana', 'cherry']
    sample_target_checklist = ['banana', 'grape', 'orange']
    result = check_element_presence(sample_query_list, sample_target_checklist)
    print(result)