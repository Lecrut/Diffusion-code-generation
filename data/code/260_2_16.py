def find_common_elements(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets.")
    
    return set1.intersection(set2)

if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(find_common_elements(set_a, set_b))
    
    set_c = {10, 20, 30}
    set_d = {40, 50, 60}
    print(find_common_elements(set_c, set_d))
    
    set_e = {7, 8, 9}
    set_f = {9, 8, 7}
    print(find_common_elements(set_e, set_f))