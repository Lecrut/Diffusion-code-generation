def is_element_in_list(primary_list, secondary_list):
    primary_set = set(primary_list)
    secondary_set = set(secondary_list)
    return not secondary_set.isdisjoint(primary_set)

if __name__ == '__main__':
    sample_primary = [10, 25, 37, 42, 50]
    sample_secondary = [37, 60, 75]
    result = is_element_in_list(sample_primary, sample_secondary)
    print(f"Primary List: {sample_primary}")
    print(f"Secondary List: {sample_secondary}")
    print(f"Does the secondary list contain any element from the primary list? {result}")