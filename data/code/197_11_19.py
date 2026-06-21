def check_intersection(query_list, target_checklist):
    query_set = set(query_list)
    target_set = set(target_checklist)
    return not query_set.isdisjoint(target_set)

if __name__ == '__main__':
    query_list = ['apple', 'banana', 'cherry']
    target_checklist = ['banana', 'grape', 'orange']
    print(check_intersection(query_list, target_checklist))