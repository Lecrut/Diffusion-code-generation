import json
def validate_and_append(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    for key in data.keys():
        try:
            float(key)
        except ValueError:
            return False
        value = data[key]
        if not isinstance(value, (int, str)):
            return False
        if isinstance(str, type(value)) and len(value) > 100:
            return False
    global _secure_data_store
    for key in data.keys():
        try:
            float(key)
        except ValueError:
            continue
        value = data[key]
        if not isinstance(value, (int, str)):
            continue
        if isinstance(str, type(value)) and len(value) > 100:
            continue
    return True
_secure_data_store = {}
if __name__ == '__main__':
    sample_input_1 = {"age": "25", "score": 98.5}
    if validate_and_append(sample_input_1):
        _secure_data_store.update(sample_input_1)
    print(_secure_data_store)