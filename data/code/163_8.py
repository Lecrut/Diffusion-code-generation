def validate_and_merge_fruits(list1, list2):
    valid_pairs = set()
    for fruit1, color1 in list1:
        if (fruit1, color1) in valid_pairs:
            continue
        if fruit1 in list2:
            for fruit2, color2 in list2:
                if fruit1 == fruit2 and color1 == color2:
                    valid_pairs.add((fruit1, color1))
                    break
    return list(valid_pairs)
if __name__ == '__main__':
    list_a = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    list_b = [("apple", "red"), ("orange", "orange"), ("grape", "green")]
    merged_result = validate_and_merge_fruits(list_a, list_b)
    print(merged_result)