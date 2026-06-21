def check_elements(query_list, target_checklist):
    return bool(set(query_list) & set(target_checklist))

if __name__ == '__main__':
    query = ['apple', 'banana', 'cherry']
    checklist = ['banana', 'date', 'fig']
    print(check_elements(query, checklist))