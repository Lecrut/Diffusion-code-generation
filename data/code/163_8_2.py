def validate_and_merge_fruits(list1, list2):
    valid_pairs = set()
    for fruit1, color1 in list1:
        if fruit1 in list2:
            for fruit2, color2 in list2:
                if fruit1 == fruit2:
                    valid_pairs.add((fruit1, color1))
    merged_list = []
    for fruit1, color1 in list1:
        if (fruit1, color1) in valid_pairs:
            merged_list.append((fruit1, color1))
    return merged_list
if __name__ == '__main__':
    list_a = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    list_b = [("banana", "green"), ("apple", "red"), ("orange", "orange")]
    result = validate_and_merge_fruits(list_a, list_b)
    print(result)