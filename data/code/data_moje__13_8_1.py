from collections import defaultdict

def get_or_init_with_composite_key(default_dict, key, factory):
    if key not in default_dict:
        default_dict[key] = factory()
    return default_dict[key]

if __name__ == '__main__':
    dd = defaultdict(list)
    composite_key = ('user', 'prefs', 'theme')
    factory = lambda: {'dark_mode': True, 'font_size': 14}
    result = get_or_init_with_composite_key(dd, composite_key, factory)
    print(result)
    result2 = get_or_init_with_composite_key(dd, composite_key, factory)
    print(result2)
    print(result is result2)