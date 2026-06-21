def check_elements(query_list, target_checklist):
    query_set = set(query_list)
    target_set = set(target_checklist)
    return not query_set.isdisjoint(target_set)

if __name__ == '__main__':
    sample_query = ['apple', 'banana', 'cherry']
    sample_target = ['banana', 'grape', 'orange']
    print(check_elements(sample_query, sample_target))