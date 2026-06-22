from collections import defaultdict

def get_value_with_composite_key(d, key, factory):
    if key not in d:
        d[key] = factory()
    return d[key]

if __name__ == '__main__':
    d = defaultdict(list)
    composite_key = ('user', 'preferences')
    factory = lambda: {'theme': 'dark', 'notifications': True}
    result = get_value_with_composite_key(d, composite_key, factory)
    print(result)