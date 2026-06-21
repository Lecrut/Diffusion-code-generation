def validate_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All elements must be strings.")
    return [name.capitalize() for name in names]

def group_names_by_first_letter(names):
    validated_names = validate_names(names)
    grouped = {}
    for name in validated_names:
        first_letter = name[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(name)
    return grouped

if __name__ == '__main__':
    sample_names = ["alice", "bob", "charlie", "david", "eve"]
    result = group_names_by_first_letter(sample_names)
    print(result)