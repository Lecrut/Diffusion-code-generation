def validate_lists(list_a, list_b):
    if not all(isinstance(item, str) for item in list_a + list_b):
        raise ValueError("Both lists must contain only strings.")
    return list_a, list_b

def concatenate_lists(list_a, list_b):
    return [item for sublist in (list_a, list_b) for item in sublist]

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry"]
    list_b = ["date", "elderberry", "fig"]
    validated_lists = validate_lists(list_a, list_b)
    result = concatenate_lists(*validated_lists)
    print(result)