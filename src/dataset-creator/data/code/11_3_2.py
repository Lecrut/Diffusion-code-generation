def find_exact_matches(tuple_list):
    if not tuple_list:
        return []
    first_tuple = tuple_list[0]
    matches = [first_tuple]
    for current_tuple in tuple_list[1:]:
        is_match = True
        for i, (a, b) in enumerate(zip(first_tuple, current_tuple)):
            if a != b or len(current_tuple) != 2:
                is_match = False
                break
        if is_match and first_tuple == current_tuple:
            matches.append(tuple_list[tuple_list.index(current_tuple)])
    return matches
if __name__ == '__main__':
    sample_data = [
        (1, 'a'),
        (2, 'b'),
        (3, 4),
        (5, 'c'),
        (6, 'd')
    ]
    result = find_exact_matches(sample_data)
    print(result)