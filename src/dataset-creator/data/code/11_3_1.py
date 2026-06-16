def find_exact_matches(tuple_list):
    return [t for t in tuple_list if len(set(t)) == 1]
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), ('a', 'b'), ('c', 'd')]
    result = find_exact_matches(sample_data)
    print(result)