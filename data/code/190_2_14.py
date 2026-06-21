def contains_element(primary_list, secondary_list):
    return bool(set(primary_list) & set(secondary_list))

if __name__ == '__main__':
    primary = [10, 25, 37, 42, 50]
    secondary = [37, 60, 75]
    result = contains_element(primary, secondary)
    print(f"Primary List: {primary}")
    print(f"Secondary List: {secondary}")
    print(f"Does the primary list contain any element from the secondary list? {result}")