from collections import defaultdict

def get_or_default(dd, key, factory):
    return dd[key] if key in dd else dd.setdefault(key, factory())

if __name__ == '__main__':
    dd = defaultdict(list)
    result = get_or_default(dd, 'missing', list)
    print(result)
    dd['existing'] = [1, 2]
    result2 = get_or_default(dd, 'existing', list)
    print(result2)