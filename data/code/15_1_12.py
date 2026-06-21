def get_penultimate_item(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate_item(sample_list))
    try:
        get_penultimate_item([1])
    except ValueError as e:
        print(e)