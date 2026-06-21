def elements_in_common(query_list, target_checklist):
    query_set = set(query_list)
    checklist_set = set(target_checklist)
    return not query_set.isdisjoint(checklist_set)

if __name__ == '__main__':
    query_list = ['apple', 'banana', 'cherry']
    target_checklist = ['banana', 'grape', 'orange']
    print(f"Elements in common: {elements_in_common(query_list, target_checklist)}")