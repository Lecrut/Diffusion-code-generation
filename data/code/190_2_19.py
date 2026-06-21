def contains_element(primary_list, secondary_list):
    primary_set = set(primary_list)
    return any(element in primary_set for element in secondary_list)

if __name__ == '__main__':
    sample_primary = [10, 25, 37, 42, 50]
    sample_secondary = [37, 60, 75]
    result = contains_element(sample_primary, sample_secondary)
    print(f"Primary List: {sample_primary}")
    print(f"Secondary List: {sample_secondary}")
    print(f"Does the secondary list contain any element from the primary list? {result}")