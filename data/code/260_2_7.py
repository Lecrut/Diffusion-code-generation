def find_common_elements(set1, set2):
    return set1.intersection(set2)

if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(find_common_elements(set_a, set_b))