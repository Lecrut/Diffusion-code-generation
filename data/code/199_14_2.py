import collections
def group_names_by_first_letter(names):
    grouped = collections.defaultdict(list)
    for name in names:
        if name:
            first_letter = name[0].upper()
            grouped[first_letter].append(name)
    return dict(grouped)
if __name__ == '__main__':
    sample_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Anna",
        "David",
        "Barbara",
        "Eve",
        "Charles"
    ]
    result = group_names_by_first_letter(sample_names)
    print(result)