from collections import defaultdict

def get_or_set_with_factory(d, key, factory):
    if key not in d:
        d[key] = factory()
    return d[key]

if __name__ == '__main__':
    d = defaultdict()
    composite_key = ('user', 'profile')
    factory = lambda: {'name': '', 'age': 0}
    result = get_or_set_with_factory(d, composite_key, factory)
    print(result)
    result['name'] = 'Alice'
    result['age'] = 30
    second_access = get_or_set_with_factory(d, composite_key, factory)
    print(second_access)
    print(d[composite_key] is second_access)