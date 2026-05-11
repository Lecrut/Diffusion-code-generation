import itertools
def group_overlapping(data, categories):
    groups = {}
    for item in data:
        assigned = False
        for category in categories:
            if category in item:
                if category not in groups:
                    groups[category] = []
                groups[category].append(item)
                assigned = True
        if not assigned:
            unassigned_group = "unassigned"
            if unassigned_group not in groups:
                groups[unassigned_group] = []
            groups[unassigned_group].append(item)
    return groups
if __name__ == '__main__':
    data_entries = [
        "apple banana",
        "banana orange",
        "apple orange",
        "grape kiwi",
        "apple kiwi"
    ]
    categories_to_check = [
        "apple",
        "banana",
        "orange",
        "grape"
    ]
    grouped_data = group_overlapping(data_entries, categories_to_check)
    for category, items in grouped_data.items():
        print(f"--- {category} ---")
        for item in items:
            print(item)
        print()