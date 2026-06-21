from collections import defaultdict

def get_composite_value(default_dict, key, factory):
    if key not in default_dict:
        default_dict[key] = factory()
    return default_dict[key]

if __name__ == '__main__':
    dd = defaultdict(lambda: None)
    composite_key = (1, 2, "hello")
    factory_func = lambda: 42
    result = get_composite_value(dd, composite_key, factory_func)
    print(result)
    print(dd[composite_key])
    new_key = (3, 4, "world")
    new_factory = lambda: [1, 2, 3]
    result2 = get_composite_value(dd, new_key, new_factory)
    print(result2)
    print(dd[new_key])