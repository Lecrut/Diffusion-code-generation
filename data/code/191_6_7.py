def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def combine_lists(list_alpha, list_beta):
    validated_list_a, validated_list_b = validate_lists(list_alpha, list_beta)
    combined = []
    for item in validated_list_a:
        combined.append(item)
    for item in validated_list_b:
        combined.append(item)
    return combined

if __name__ == '__main__':
    sample_list1 = ["apple", "banana"]
    sample_list2 = ["cherry", "date"]
    result = combine_lists(sample_list1, sample_list2)
    print(result)