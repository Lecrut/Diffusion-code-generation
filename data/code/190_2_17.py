def has_common_element(primary_list, secondary_list):
    return bool(set(primary_list) & set(secondary_list))
if __name__ == '__main__':
    primary = [1, 2, 3, 4, 5]
    secondary = [6, 7, 8, 9, 0]
    print(has_common_element(primary, secondary))
    primary = [1, 2, 3, 4, 5]
    secondary = [5, 6, 7, 8, 9]
    print(has_common_element(primary, secondary))