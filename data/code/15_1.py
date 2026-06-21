def get_penultimate(item_list):
    if len(item_list) < 2:
        raise ValueError("List must contain at least two elements")
    return item_list[-2]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    result = get_penultimate(test_list)
    print(result)
    try:
        get_penultimate([1])
    except ValueError as e:
        print(e)