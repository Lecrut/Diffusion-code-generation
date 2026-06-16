import json
def deep_equality_check(obj1: any, obj2: any) -> bool:
    if type(obj1) != type(obj2):
        return False
    try:
        iter(obj1)
    except TypeError:
        return obj1 == obj2
    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2 or not deep_equality_check(obj1[key], obj2[key]):
                return False
        return True
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equality_check(obj1[i], obj2[i]):
                return False
        return True
    else:
        try:
            json_str = json.dumps((obj1,), sort_keys=True) if isinstance(obj1, dict) else str(obj1).replace("'", '"')
            return json.loads(json_str) == json.loads(str(obj2))
        except (TypeError, ValueError):
            return obj1 == obj2
if __name__ == '__main__':
    sample_data_1 = {
        "user": {"id": 42, "details": ["Alice", "Bob"]},
        "settings": {"theme": "dark"},
        "tags": set(["python", "code"])
    }
    sample_data_2 = {
        "user": {"id": 42, "details": ["Alice", "Bob"]},
        "settings": {"theme": "light"},
        "tags": set(["python", "code"])
    }
    print(deep_equality_check(sample_data_1, sample_data_2))