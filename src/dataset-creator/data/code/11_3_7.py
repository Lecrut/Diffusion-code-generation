def find_exact_matches(tuple_list):
    if not tuple_list:
        return []
    result = [tuple_list[0]]
    for item in tuple_list[1:]:
        if all(a == b for a, b in zip(result[-1], item)):
            result.append(item)
    return result
if __name__ == '__main__':
    data = [(1, 2), (3, 4), (5, 6)]
    print(find_exact_matches(data))