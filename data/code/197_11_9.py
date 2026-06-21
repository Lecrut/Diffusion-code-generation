def check_intersection(query_list, target_checklist):
    return bool(set(query_list) & set(target_checklist))

if __name__ == '__main__':
    query = ['apple', 'banana', 'cherry']
    checklist = ['banana', 'grape', 'orange']
    print(check_intersection(query, checklist))