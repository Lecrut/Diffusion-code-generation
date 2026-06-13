class ComplexObject:
    def __init__(self, id, category, details):
        self.id = id
        self.category = category
        self.details = details
def group_objects(objects, key_path):
    groups = {}
    for obj in objects:
        current_key = None
        temp = obj
        path_parts = key_path.split('.')
        for part in path_parts:
            if isinstance(temp, dict):
                if part in temp:
                    current_key = temp[part]
                    temp = temp[part]
                else:
                    current_key = None
                    break
            elif hasattr(temp, part):
                current_key = getattr(temp, part)
                temp = getattr(temp, part)
            else:
                current_key = None
                break
        if current_key is not None:
            if current_key not in groups:
                groups[current_key] = []
            groups[current_key].append(obj)
        else:
            groups["__missing__"] = groups.get("__missing__", []) + [obj]
    return groups
if __name__ == '__main__':
    data = [
        ComplexObject(1, 'A', {'sub': 'X'}),
        ComplexObject(2, 'B', {'sub': 'Y'}),
        ComplexObject(3, 'A', {'sub': 'Z'}),
        ComplexObject(4, 'C', {'sub': 'X'}),
        ComplexObject(5, 'A', None),
        ComplexObject(6, 'D', {'sub': 'W'})
    ]
    key = 'category.details.sub'
    grouped_data = group_objects(data, key)
    print(grouped_data)