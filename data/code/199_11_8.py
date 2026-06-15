def manipulate_names(names, manipulation_type):
    if not names:
        return []
    n = len(names)
    if manipulation_type == 'reverse':
        return names[::-1]
    elif manipulation_type == 'sort_alphabetical':
        sorted_names = sorted(names)
        return sorted_names
    elif manipulation_type == 'capitalize':
        modified_names = []
        for name in names:
            if name:
                modified_names.append(name[0].upper() + name[1:].lower())
            else:
                modified_names.append("")
        return modified_names
    else:
        return names
if __name__ == '__main__':
    sample_names = ["alice", "bob", "charlie", "david"]
    result_reverse = manipulate_names(sample_names, 'reverse')
    print(f"Original: {sample_names}")
    print(f"Reverse: {result_reverse}")
    result_sort = manipulate_names(sample_names, 'sort_alphabetical')
    print(f"Sort Alphabetical: {result_sort}")
    result_capitalize = manipulate_names(sample_names, 'capitalize')
    print(f"Capitalize: {result_capitalize}")
    result_unknown = manipulate_names(sample_names, 'unknown_op')
    print(f"Unknown Operation: {result_unknown}")
    sample_names_2 = ["Zoe", "adam", "B", "Charlie"]
    result_reverse_2 = manipulate_names(sample_names_2, 'reverse')
    print(f"\nOriginal: {sample_names_2}")
    print(f"Reverse: {result_reverse_2}")