def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    return input_list

def find_unique_items(list1, list2):
    validated_list1 = validate_input(list1)
    validated_list2 = validate_input(list2)
    
    set1 = set(validated_list1)
    set2 = set(validated_list2)
    
    unique_items = set1.difference(set2)
    return list(unique_items)

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8]
    try:
        result = find_unique_items(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)