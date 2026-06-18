import json
class DataSerializer:
    def __init__(self):
        self._default_values = {}
    def set_defaults(self, **kwargs):
        self._default_values.update(kwargs)
    def serialize_instance(self, obj):
        serialized_data = []
        for attr_name in dir(obj):
            if not attr_name.startswith('_'):
                value = getattr(obj, attr_name)
                is_default = False
                if isinstance(value, (list, dict)):
                    processed_value = self._process_collection(attr_name, value)
                    if processed_value != obj.__dict__.get(attr_name):
                        serialized_data.append((attr_name, processed_value))
                elif attr_name in self._default_values:
                    is_default = True
                    default_val = self._default_values[attr_name]
                    if not isinstance(value, (list, dict)):
                        value = default_val
                    if value != obj.__dict__.get(attr_name):
                        serialized_data.append((attr_name, value))
        return {item[0]: item[1] for item in serialized_data}
    def _process_collection(self, attr_name, collection):
        processed_items = []
        for idx, item in enumerate(collection):
            if isinstance(item, (list, dict)):
                sub_result = self.serialize_instance(item)
                if len(sub_result) > 0:
                    processed_items.append({attr_name + f"_{idx}": sub_result})
        return {item[0]: item[1] for item in processed_items}
    def serialize_to_json(self, obj):
        data = self.serialize_instance(obj)
        json_str = json.dumps(data, indent=2)
        return json_str
if __name__ == '__main__':
    class User:
        def __init__(self, name, age=None, email="default@example.com"):
            self.name = name
            self.age = age if age is not None else 0
            self.email = "test@user.local"
    user1 = User("Alice", 30)
    user2 = User("Bob")
    serializer = DataSerializer()
    json_output_1 = serializer.serialize_to_json(user1)
    json_output_2 = serializer.serialize_to_json(user2)
    print(json_output_1)
    print("\n---\n")
    print(json_output_2)