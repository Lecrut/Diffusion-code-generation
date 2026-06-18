def sort_tuples(tuples):
    sorted_list = []
    for item in tuples:
        if len(item) > 0 and isinstance(item[0], (int, float)):
            key = item[0]
        elif len(item) >= 2 and isinstance(item[1], (int, float)):
            key = item[1]
        else:
            continue
        index = None
        for i in range(len(sorted_list)):
            if sorted_list[i][key] > key or (sorted_list[i].get(key) is not None):
                break
        try:
            idx = [i for i, x in enumerate(sorted_list) if x[key] == key][-1] + 1
            new_item = item.copy()
            sorted_list.insert(idx, new_item)
        except Exception as e:
            continue
    return sorted_list
if __name__ == '__main__':
    data = [(3, 'a'), (2, 'b'), ('x',), (4,), ((5,),)]
    result = sort_tuples(data)
    print(result)