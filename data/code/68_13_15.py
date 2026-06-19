def find_unique_elements(primary_list, secondary_list):
    primary_set = set(primary_list)
    secondary_set = set(secondary_list)
    unique_elements = primary_set.difference(secondary_set)
    return list(unique_elements)

if __name__ == '__main__':
    sample_primary_list = [100, 200, 300, 400, 500]
    sample_secondary_list = [300, 400, 600, 700, 800]
    unique_result = find_unique_elements(sample_primary_list, sample_secondary_list)
    print(unique_result)