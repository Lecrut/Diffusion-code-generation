class ComplexObject:
    def __init__(self, id, category, details):
        self.id = id
        self.category = category
        self.details = details
def group_objects_by_nested_attribute(objects, key_path):
    groups = {}
    for obj in objects:
        current_level = obj
        found = True
        for key in key_path:
            if isinstance(current_level, dict) and key in current_level:
                current_level = current_level[key]
            else:
                found = False
                break
        if found:
            group_key = current_level
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(obj)
    return groups
if __name__ == '__main__':
    data = [
        ComplexObject(1, 'A', {'sub': 'X', 'level2': 10}),
        ComplexObject(2, 'B', {'sub': 'Y'}),
        ComplexObject(3, 'A', {'sub': 'Z', 'level2': 20}),
        ComplexObject(4, 'C', {'sub': 'X'}),
        ComplexObject(5, 'B', {'sub': 'W'})
    ]
    key_path = ['category', 'sub']
    grouped_data = group_objects_by_nested_attribute(data, key_path)
    print(grouped_data)