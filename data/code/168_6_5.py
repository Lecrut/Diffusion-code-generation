class FlexibleGrouper:
    def __init__(self):
        self.groups = {}
    def group_data(self, data_list, categories):
        for item in data_list:
            assigned = False
            for category in categories:
                if category in item:
                    if category not in self.groups:
                        self.groups[category] = []
                    self.groups[category].append(item)
                    assigned = True
            if not assigned:
                self.groups["unassigned"] = self.groups.get("unassigned", [])
                self.groups["unassigned"].append(item)
    def get_groups(self):
        return self.groups
if __name__ == '__main__':
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 30, "city": "Paris"},
        {"name": "David", "age": 22, "city": "New York"}
    ]
    categories_to_check = [
        "age",
        "city"
    ]
    grouper = FlexibleGrouper()
    grouper.group_data(data, categories_to_check)
    result = grouper.get_groups()
    import json
    print(json.dumps(result, indent=4))