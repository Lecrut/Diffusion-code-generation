def print_initial_value(data):
    if not data:
        return "Empty list"
    iterator = iter(data)
    return next(iterator)

if __name__ == '__main__':
    sample_list = ["alpha", "beta", "gamma", "delta"]
    result = print_initial_value(sample_list)
    print(result)