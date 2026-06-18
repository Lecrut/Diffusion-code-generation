import json
class DynamicOrganizer:
    def __init__(self):
        self.data = {}
    def add(self, key, value_list):
        if isinstance(value_list, list) and all(isinstance(item, (list, dict)) for item in value_list):
            self.data[key] = [item.copy() if isinstance(item, dict) else item for item in value_list]
        return True
    def get(self, key):
        return self.data.get(key)
if __name__ == '__main__':
    organizer = DynamicOrganizer()
    sample_data_1 = [[1, 2], {"a": "b"}, [3]]
    sample_data_2 = [["x", "y"], ["z"]]
    organizer.add("group_a", sample_data_1)
    organizer.add("group_b", sample_data_2)
    print(json.dumps(organizer.get("group_a"), indent=4))
    print(json.dumps(organizer.get("group_b"), indent=4))