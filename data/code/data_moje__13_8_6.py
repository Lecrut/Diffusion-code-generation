from collections import defaultdict

def get_value_with_factory(d, key, factory_func):
    if key not in d:
        d[key] = factory_func()
    return d[key]

if __name__ == '__main__':
    dd = defaultdict(list)
    composite_key = ('user', 'settings')
    result = get_value_with_factory(dd, composite_key, lambda: {'theme': 'dark', 'lang': 'en'})
    print(result)