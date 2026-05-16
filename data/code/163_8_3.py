def validate_and_merge_fruits(list1, list2):
    set1 = set(zip(list1, list1))
    set2 = set(zip(list2, list2))
    merged_set = set()
    for fruit1, color1 in list1:
        if (fruit1, color1) in set2:
            merged_set.add((fruit1, color1))
    for fruit2, color2 in list2:
        if (fruit2, color2) in set1:
            merged_set.add((fruit2, color2))
    return list(merged_set)
if __name__ == '__main__':
    fruits1 = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    fruits2 = [("apple", "red"), ("orange", "orange"), ("grape", "green")]
    result = validate_and_merge_fruits(fruits1, fruits2)
    print(result)