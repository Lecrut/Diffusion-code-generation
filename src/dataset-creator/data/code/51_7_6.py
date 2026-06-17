def get_first_item(items):
    if not items:
        raise ValueError("List is empty")
    return items[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    try:
        first_element = get_first_item(sample_list)
        print(first_element)
    except ValueError as e:
        print(e)