def group_items(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v2(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v3(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v4(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v5(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v6(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v7(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v8(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v9(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v10(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v11(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v12(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v13(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v14(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v15(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v16(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v17(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dict_comprehension_true_v18(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'category': 'Fruit'},
        {'item': 'Banana', 'category': 'Fruit'},
        {'item': 'Carrot', 'category': 'Vegetable'},
        {'item': 'Broccoli', 'category': 'Vegetable'},
        {'item': 'Orange', 'category': 'Fruit'},
        {'item': 'Potato', 'category': 'Vegetable'}
    ]
    result = group_items_optimized(sample_data)
    print(result)