import json
from typing import Any, Dict
class EfficientSerializer:
    def __init__(self):
        self._defaults = {}
    def set_default(self, key: str, value: Any) -> None:
        if isinstance(value, dict):
            self._defaults[key] = {k: v for k, v in value.items() if not callable(v)}
        else:
            self._defaults[key] = value
    def serialize(self, obj: Any) -> str:
        try:
            return json.dumps(obj, ensure_ascii=False, default=self._default_handler)
        except TypeError as e:
            raise ValueError(f"Serialization failed due to unsupported type or missing defaults: {e}")
    def _default_handler(self, obj: Any):
        if isinstance(obj, dict):
            result = {}
            for key in self._defaults.keys():
                default_val = self._defaults[key]
                if isinstance(default_val, dict) and obj.get(key, {}).get('nested') is not None:
                    val = {**default_val, **obj.get(key)}
                    result.update(val)
            return result
    def serialize_large_dataset(self, data_list: list) -> str:
        chunk_size = 1000
        all_json_parts = []
        for i in range(0, len(data_list), chunk_size):
            chunk = data_list[i:i + chunk_size]
            serialized_chunk = json.dumps(chunk)
            all_json_parts.append(serialized_chunk)
        return '\n'.join(all_json_parts).strip()
if __name__ == '__main__':
    serializer = EfficientSerializer()
    user_data = {
        'id': 1,
        'username': None,
        'email': 'user@example.com',
        'address': {'city': '', 'zip': ''},
        'metadata': {}
    }
    serializer.serialize(user_data)