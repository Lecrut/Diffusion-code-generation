import json
from typing import Any, Dict
class SerializableObject:
    def __init__(self, **kwargs):
        self._data = {}
        for key, value in kwargs.items():
            if isinstance(value, (list, dict)):
                self._data[key] = _deep_copy(value)
            else:
                default_map = {
                    'name': None,
                    'age': 0,
                    'active': True,
                    'scores': [],
                    'metadata': {}
                }
                if key in default_map and value is None:
                    self._data[key] = default_map[key]
                else:
                    self._data[key] = _deep_copy(value)
    def to_json(self):
        filtered_data = {k: v for k, v in self._data.items() if v is not None}
        return json.dumps(filtered_data, indent=2)
def _deep_copy(obj):
    import copy
    return copy.deepcopy(obj)
if __name__ == '__main__':
    user1 = SerializableObject(name="Alice", age=None, active=True, scores=[90, 85], metadata={"id": "U001"})
    user2 = SerializableObject(name="Bob", age=30, active=False, scores=[], metadata={})
    output_data = [user1.to_json(), user2.to_json()]
    print(json.dumps(output_data))