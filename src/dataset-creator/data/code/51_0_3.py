def find_first_element(elements):
    for element in elements:
        return element
    raise ValueError("List is empty")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        first_item = find_first_element(sample_list)
        print(first_item)
    except ValueError as exception_info:
        print(exception_info)