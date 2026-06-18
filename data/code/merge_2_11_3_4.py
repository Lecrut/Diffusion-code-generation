def find_exact_matches(tuple_list):
    if not tuple_list:
        return []
    first_tuple = tuple_list[0]
    matches = [first_tuple]
    for current in tuple_list[1:]:
        if len(current) != len(first_tuple):
            continue
        is_match = True
        for i, (a, b) in enumerate(zip(first_tuple, current)):
            a_val, b_val = first_tuple[i], current[i]
            try:
                if isinstance(a_val, float):
                    if not abs(float(a_val - b_val)) < 1e-9:
                        is_match = False
                        break
                else:
                    if a_val != b_val:
                        is_match = False
                        break
            except TypeError:
                continue
        if is_match:
            matches.append(current)
    return matches
if __name__ == '__main__':
    sample_data = [
        (1, 2.0),
        ('a', 'b'),
        (3, 4),
        (5, 6),
        (7, 8),
        (9, 10)
    ]
    result = find_exact_matches(sample_data)
    print(result)