from collections import defaultdict

def get_or_default(composite_dict, key, factory):
    if key not in composite_dict:
        composite_dict[key] = factory()
    return composite_dict[key]

if __name__ == '__main__':
    my_dict = defaultdict(list)
    result = get_or_default(my_dict, ('a', 'b'), list)
    result.append(1)
    print(result)