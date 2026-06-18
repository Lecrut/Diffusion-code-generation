def find_exact_matches(tuple_list):
    if not tuple_list:
        return []
    result = [tuple_list[0]]
    for i in range(1, len(tuple_list)):
        current_tuple = tuple_list[i]
        is_match = True
        for j in range(len(current_tuple)):
            if current_tuple[j] != result[-1][j]:
                is_match = False
                break
        if is_match:
            result.append(current_tuple)
    return result
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    matches = find_exact_matches(sample_data)
    print(matches)