def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

if __name__ == '__main__':
    sample_list1 = [42, 84, 168]
    sample_list2 = ['apple', 'banana', 'cherry']
    empty_sample_list = []

    try:
        first_element1 = get_first_element(sample_list1)
        print(f"First element of {sample_list1}: {first_element1}")
    except IndexError as e:
        print(f"Error processing {sample_list1}: {e}")

    try:
        first_element2 = get_first_element(sample_list2)
        print(f"First element of {sample_list2}: {first_element2}")
    except IndexError as e:
        print(f"Error processing {sample_list2}: {e}")

    try:
        get_first_element(empty_sample_list)
    except IndexError as e:
        print(f"Error caught for empty list: {e}")