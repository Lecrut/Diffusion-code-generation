def get_initial_value(items):
    iterator = iter(items)
    try:
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    result = get_initial_value(sample_list)
    print(result)