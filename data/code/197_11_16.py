def check_elements(query_list, target_checklist):
    if not isinstance(query_list, list) or not all((isinstance(item, str) for item in query_list)):
        raise ValueError('query_list must be a list of strings')
    if not isinstance(target_checklist, set) or not all((isinstance(item, str) for item in target_checklist)):
        raise ValueError('target_checklist must be a set of strings')
    return bool(query_list & target_checklist)
if __name__ == '__main__':
    query = ['apple', 'banana', 'cherry']
    checklist = {'banana', 'date', 'fig'}
    print(check_elements(query, checklist))