from collections import defaultdict

def get_or_initialize(composite_dict, key, factory):
    if key not in composite_dict:
        composite_dict[key] = factory()
    return composite_dict[key]

if __name__ == '__main__':
    data = defaultdict(list)
    result = get_or_initialize(data, ('A', 'B'), lambda: [1, 2, 3])
    print(result)
    result2 = get_or_initialize(data, ('A', 'B'), lambda: [4, 5, 6])
    print(result2)
    result3 = get_or_initialize(data, ('C', 'D'), lambda: [])
    print(result3)