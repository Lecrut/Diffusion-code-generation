def get_third_element(items):
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(get_third_element(sample_list))
    try:
        get_third_element([1, 2])
    except IndexError as e:
        print(e)