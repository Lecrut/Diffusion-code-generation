def manipulate_names(names, manipulation_type):
    n = len(names)
    if n == 0:
        return []
    if manipulation_type == 'reverse':
        new_names = names[::-1]
        return new_names
    elif manipulation_type == 'sort_alphabetical':
        sorted_names = sorted(names)
        return sorted_names
    elif manipulation_type == 'capitalize':
        new_names = [name.capitalize() for name in names]
        return new_names
    else:
        return names
if __name__ == '__main__':
    sample_names1 = ["alice", "bob", "charlie", "david"]
    print("Original:", sample_names1)
    result_reverse = manipulate_names(sample_names1, 'reverse')
    print("Reverse:", result_reverse)
    result_sort = manipulate_names(sample_names1, 'sort_alphabetical')
    print("Sort Alphabetical:", result_sort)
    result_capitalize = manipulate_names(sample_names1, 'capitalize')
    print("Capitalize:", result_capitalize)
    sample_names2 = ["Zoe", "apple", "Banana"]
    print("\nOriginal:", sample_names2)
    result_reverse2 = manipulate_names(sample_names2, 'reverse')
    print("Reverse:", result_reverse2)
    result_sort2 = manipulate_names(sample_names2, 'sort_alphabetical')
    print("Sort Alphabetical:", result_sort2)
    result_capitalize2 = manipulate_names(sample_names2, 'capitalize')
    print("Capitalize:", result_capitalize2)