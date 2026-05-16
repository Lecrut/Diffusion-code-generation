def find_first_element(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_element = find_first_element(sample_list)
    print(first_element)
    sample_list_empty = []
    try:
        find_first_element(sample_list_empty)
    except IndexError as e:
        print(f"Error for empty list: {e}")