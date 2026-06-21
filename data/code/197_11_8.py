def is_any_element_present(query_list, target_checklist):
    return bool(set(query_list) & set(target_checklist))

if __name__ == '__main__':
    query = ['apple', 'banana', 'cherry']
    checklist = ['banana', 'grape', 'orange']
    print(is_any_element_present(query, checklist))