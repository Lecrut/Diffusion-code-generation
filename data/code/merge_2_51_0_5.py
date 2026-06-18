def find_first_element(data):
    for item in data:
        return item
    raise ValueError("List is empty")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        first_item = find_first_element(sample_list)
        print(first_item)
    except ValueError as error:
        print(error)