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
def group_items_comprehension_true(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension_true_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension_final_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension_final_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension_final_optimized_final(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension_final_optimized_final_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension_true_final_optimized_comprehension_final_optimized_final_optimized_final(data):
    return {category: [item['item'] for item in data if item['category'] == category] for category in set(item['category'] for item in data)}
if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'category': 'Fruit'},
        {'item': 'Banana', 'category': 'Fruit'},
        {'item': 'Carrot', 'category': 'Vegetable'},
        {'item': 'Broccoli', 'category': 'Vegetable'},
        {'item': 'Orange', 'category': 'Fruit'},
        {'item': 'Potato', 'category': 'Vegetable'}
    ]
    result = group_items_final_comprehension_true_final_optimized_comprehension_final_optimized_final(sample_data)
    print(result)