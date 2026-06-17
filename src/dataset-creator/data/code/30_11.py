import copy
class DynamicOrganizer:
    def __init__(self):
        self._data = {}
    def add(self, key, value_list):
        if not isinstance(value_list, list):
            raise TypeError("Value must be a list")
        self._data[key] = copy.deepcopy(value_list)
    def get_all_keys(self):
        return sorted(list(self._data.keys()))
    def __repr__(self):
        items = [f"{k}: {v}" for k, v in self._data.items()]
        return f"DynamicOrganizer({', '.join(items)})"
if __name__ == '__main__':
    organizer = DynamicOrganizer()
    sample_inputs = [
        ("numbers", [1, 2, 3]),
        ("strings", ["hello", "world"]),
        ("mixed", [True, None, {"a": 1}])
    ]
    for key, value in sample_inputs:
        organizer.add(key, value)
    print(organizer.get_all_keys())
    print(repr(organizer))