def find_exact_matches(tuples_list):
    if not tuples_list:
        return []
    first_tuple = tuple(tuples_list[0])
    matches = [first_tuple]
    for i in range(1, len(tuples_list)):
        current_tuple = tuple(tuples_list[i])
        is_match = True
        if len(first_tuple) != len(current_tuple):
            continue
        for j in range(len(first_tuple)):
            if first_tuple[j] != current_tuple[j]:
                is_match = False
                break
        if is_match:
            matches.append(tuple(tuples_list[i]))
    return matches
if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6),
        (7, 8)
    ]
    result = find_exact_matches(sample_data)
    print(result)