def find_exact_matches(tuple_list):
    if not tuple_list:
        return []
    first_tuple = tuple_list[0]
    matches = [t for t in tuple_list if t == first_tuple]
    return matches
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    target_value = (3, 4)
    result = find_exact_matches(sample_data if sample_data == [target_value] else [])
    print(result)