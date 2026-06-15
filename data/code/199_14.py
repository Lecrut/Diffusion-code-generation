def group_names(names):
    grouped = {}
    for name in names:
        if name:
            first_letter = name[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(name)
    return grouped
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Anna", "David", "Betty"]
    result = group_names(sample_names)
    print(result)