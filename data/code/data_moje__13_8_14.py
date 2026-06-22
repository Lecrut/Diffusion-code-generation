import collections

def get_value_with_composite_key(dd, key, factory):
    if key in dd:
        return dd[key]
    value = factory()
    dd[key] = value
    return value

def main():
    dd = collections.defaultdict(lambda: [])
    key1 = ("a", 1)
    key2 = ("b", 2)
    factory_func = lambda: {"count": 0}
    val1 = get_value_with_composite_key(dd, key1, factory_func)
    val2 = get_value_with_composite_key(dd, key1, factory_func)
    val3 = get_value_with_composite_key(dd, key2, factory_func)
    print(val1)
    print(val2)
    print(val3)
    print(dd)

if __name__ == '__main__':
    main()