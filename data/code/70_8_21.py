def check_endpoints(iterable):
    endpoints = {
        "empty": (None, None),
        "single": lambda x: (x[0], x[0]),
        "multiple": lambda x: (x[0], x[-1])
    }
    try:
        items = list(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    if not items:
        return endpoints["empty"]
    if len(items) == 1:
        return endpoints["single"](items)
    return endpoints["multiple"](items)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first, last = check_endpoints(sample_list)
    print(f"First: {first}, Last: {last}")
    
    empty_list = []
    first, last = check_endpoints(empty_list)
    print(f"Empty - First: {first}, Last: {last}")
    
    single_item = [99]
    first, last = check_endpoints(single_item)
    print(f"Single - First: {first}, Last: {last}")
    
    string_sample = "Python"
    first, last = check_endpoints(string_sample)
    print(f"String - First: {first}, Last: {last}")