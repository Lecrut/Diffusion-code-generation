def shared_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.intersection(set_b)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    shared = shared_elements(sample_list_a, sample_list_b)
    print(shared)