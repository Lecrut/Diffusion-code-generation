from collections import defaultdict

def get_value_with_composite_key(default_dict, key, factory):
    if key not in default_dict:
        default_dict[key] = factory()
    return default_dict[key]

if __name__ == '__main__':
    d = defaultdict(list)
    composite_key = ("user", 1)
    result = get_value_with_composite_key(d, composite_key, lambda: [])
    result.append(42)
    print(result)