def retrieve_second_element(items):
    if len(items) < 2:
        raise ValueError("The list must contain at least two elements.")
    return items[1]

if __name__ == '__main__':
    demo_list = [9, 18, 27, 36, 45]
    try:
        second_value = retrieve_second_element(demo_list)
        print(second_value)
    except ValueError as e:
        print(e)