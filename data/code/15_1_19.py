def get_penultimate(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate(sample_list))
    empty_list = []
    try:
        print(get_penultimate(empty_list))
    except ValueError as e:
        print(e)
    single_list = [100]
    try:
        print(get_penultimate(single_list))
    except ValueError as e:
        print(e)
    two_items = ["a", "b"]
    print(get_penultimate(two_items))