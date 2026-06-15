class ComplexObject:
    def __init__(self, name, category, details):
        self.name = name
        self.category = category
        self.details = details
def group_objects(objects, key_path):
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
        ComplexObject("Alice", "A", {"score": 90, "level": "High"}),
        ComplexObject("Bob", "B", {"score": 85, "level": "Medium"}),
        ComplexObject("Charlie", "A", {"score": 92, "level": "High"}),
        ComplexObject("David", "C", {"score": 78, "level": "Low"}),
        ComplexObject("Eve", "B", {"score": 88}),
        ComplexObject("Frank", "A", {"score": 95, "level": "High"})
    ]
    key_path = ["category", "details", "level"]
    grouped_data = group_objects(data, key_path)
    print(grouped_data)