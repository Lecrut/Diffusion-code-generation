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
            unassigned_group = "Unassigned"
            if unassigned_group not in groups:
                groups[unassigned_group] = []
            groups[unassigned_group].append(item)
    return groups
if __name__ == '__main__':
    data_entries = [
        "apple_red_fruit",
        "banana_yellow_fruit",
        "carrot_orange_vegetable",
        "lettuce_green_vegetable",
        "grape_purple_fruit",
        "broccoli_green_vegetable",
        "spinach_green_vegetable"
    ]
    categories_list = [
        "fruit",
        "vegetable",
        "red",
        "green"
    ]
    grouped_data = group_overlapping(data_entries, categories_list)
    print(grouped_data)