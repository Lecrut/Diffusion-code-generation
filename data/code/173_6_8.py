def group_data(data, key_func):
    if not callable(key_func):
        raise ValueError("key_func must be a callable function")
    
    grouped = {}
    for item in data:
        key = key_func(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped

def group_generator(data, key_func):
    if not callable(key_func):
        raise ValueError("key_func must be a callable function")
    
    grouped = {}
    for item in data:
        key = key_func(item)
        if key not in grouped:
            grouped[key] = []
        yield (grouped[key], item)

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]
    
    for group_key, item in group_generator(sample_data, lambda x: x.split(',')[2]):
        print(f"Group {group_key}: {item}")