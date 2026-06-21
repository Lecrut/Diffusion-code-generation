def is_any_element_present(query_list, target_checklist):
    query_set = set(query_list)
    target_set = set(target_checklist)
    return not query_set.isdisjoint(target_set)

if __name__ == '__main__':
    sample_query_list = [1, 2, 3, 4]
    sample_target_checklist = [5, 6, 7, 8]
    print(is_any_element_present(sample_query_list, sample_target_checklist))