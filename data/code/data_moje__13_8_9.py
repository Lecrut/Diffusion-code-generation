from collections import defaultdict

def get_or_init(default_dict, key, factory):
    if key not in default_dict:
        default_dict[key] = factory()
    return default_dict[key]

if __name__ == '__main__':
    data = defaultdict(list)
    composite_key = ("user_123", "action_log")
    value = get_or_init(data, composite_key, lambda: {"timestamp": 0, "count": 0})
    value["timestamp"] = 1678888888
    value["count"] += 1
    print(data[composite_key])