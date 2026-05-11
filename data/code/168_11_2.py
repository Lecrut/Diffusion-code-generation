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
def group_items_comprehension_dict_comprehension(data):
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
def group_items_optimized_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension_pure(data):
    return {category: [item['item'] for item in data if item['category'] == category] for category in {item['category'] for item in data}}
def group_items_final_optimized(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_dictionary_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_final_comprehension(data):
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
    result = group_items_final(sample_data)
    print(result)