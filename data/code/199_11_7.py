def manipulate_names(names, manipulation_type):
    if not names:
        return []
    n = len(names)
    if manipulation_type == 'reverse':
        result = names[::-1]
        return result
    elif manipulation_type == 'sort_alphabetical':
        sorted_names = sorted(names)
        return sorted_names
    elif manipulation_type == 'capitalize':
        result = []
        for name in names:
            if name:
                result.append(name[0].upper() + name[1:].lower())
            else:
                result.append("")
        return result
    else:
        return names
if __name__ == '__main__':
    sample_names = ["alice", "bob", "charlie", "david", "eve"]
    print("Original Names:", sample_names)
    reversed_names = manipulate_names(sample_names, 'reverse')
    print("Reversed Names:", reversed_names)
    sorted_names = manipulate_names(sample_names, 'sort_alphabetical')
    print("Sorted Alphabetical Names:", sorted_names)
    capitalized_names = manipulate_names(sample_names, 'capitalize')
    print("Capitalized Names:", capitalized_names)
    unknown_manipulation = manipulate_names(sample_names, 'unknown')
    print("Unknown Manipulation Result (No change):", unknown_manipulation)