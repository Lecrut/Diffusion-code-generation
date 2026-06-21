def contains_element(primary_list, secondary_list):
    primary_set = set(primary_list)
    return bool(primary_set.intersection(secondary_list))

if __name__ == '__main__':
    sample_primary = [10, 25, 37, 42, 50]
    sample_secondary = [37, 60, 75]
    result = contains_element(sample_primary, sample_secondary)
    print(f"Primary List: {sample_primary}")
    print(f"Secondary List: {sample_secondary}")
    print(f"Does the primary list contain any element from the secondary list? {result}")