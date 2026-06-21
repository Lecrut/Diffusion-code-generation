def group_names_by_first_letter(names):
    grouped = {}
    for name in names:
        first_letter = name[0].upper()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(name)
    return grouped

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print(group_names_by_first_letter(sample_names))