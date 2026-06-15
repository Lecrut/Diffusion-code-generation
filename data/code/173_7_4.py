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
        for part in key_path:
            if isinstance(current_level, dict) and part in current_level:
                current_level = current_level[part]
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
        ComplexObject(1, 'A', {'sub': 'X', 'value': 100}),
        ComplexObject(2, 'B', {'sub': 'Y', 'value': 200}),
        ComplexObject(3, 'A', {'sub': 'Z', 'value': 300}),
        ComplexObject(4, 'C', {'sub': 'X', 'value': 400}),
        ComplexObject(5, 'B', {'sub': 'W'}),
        ComplexObject(6, 'D', {})
    ]
    key_path = ['category', 'details', 'sub']
    grouped_data = group_objects_by_nested_attribute(data, key_path)
    print(grouped_data)