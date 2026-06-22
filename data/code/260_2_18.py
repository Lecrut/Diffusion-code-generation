def find_common_elements(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets")
    return set1 & set2

if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(find_common_elements(set_a, set_b))