def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    try:
        print(get_last_item(sample_data))
    except IndexError as e:
        print(e)

    empty_data = []
    try:
        print(get_last_item(empty_data))
    except IndexError as e:
        print(e)