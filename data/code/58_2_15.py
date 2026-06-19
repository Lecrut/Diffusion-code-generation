def get_first_item(data_list):
    if not data_list:
        raise IndexError("The list is empty and does not contain any items.")
    return data_list[0]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25]
    sample_list_2 = []

    try:
        first_item_1 = get_first_item(sample_list_1)
        print(f"The first item in sample_list_1 is: {first_item_1}")
    except IndexError as e:
        print(e)

    try:
        first_item_2 = get_first_item(sample_list_2)
        print(f"The first item in sample_list_2 is: {first_item_2}")
    except IndexError as e:
        print(e)