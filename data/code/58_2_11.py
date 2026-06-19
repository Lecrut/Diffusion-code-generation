def fetch_first_element(data_list):
    if not data_list:
        raise IndexError("The list is empty and does not contain any elements.")
    return data_list[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    empty_list = []

    try:
        first_element = fetch_first_element(sample_list)
        print(f"The first element of the sample list is: {first_element}")
    except IndexError as e:
        print(f"Error fetching from sample list: {e}")

    try:
        first_element_empty = fetch_first_element(empty_list)
        print(f"The first element of the empty list is: {first_element_empty}")
    except IndexError as e:
        print(f"Error fetching from empty list: {e}")