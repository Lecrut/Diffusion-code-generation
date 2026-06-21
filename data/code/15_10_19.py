def get_penultimate_element(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)
    try:
        get_penultimate_element([1])
    except ValueError as e:
        print(e)