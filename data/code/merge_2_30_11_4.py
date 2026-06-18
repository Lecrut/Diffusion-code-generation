import json
class DynamicOrganizer:
    def __init__(self):
        self.data = {}
    def add_entry(self, key, value_list):
        if isinstance(value_list, list):
            try:
                validated_value = [item for item in value_list]
            except TypeError:
                raise ValueError(f"Value at {key} must be a list of items.")
            self.data[key] = json.dumps(validated_value)
    def get_entry(self, key):
        return json.loads(self.data.get(key)) if key in self.data else None
if __name__ == '__main__':
    organizer = DynamicOrganizer()
    sample_data = [10.5, "hello", True]
    nested_items = [[1, 2], ["a", "b"], {"x": 1}]
    try:
        organizer.add_entry("scores", sample_data)
        organizer.add_entry("tags", nested_items[0])
        organizer.add_entry("details", json.dumps(nested_items))
        print(organizer.get_entry("scores"))
        print(organizer.get_entry("tags"))
    except Exception as e:
        print(f"Error occurred: {e}")