def validate_list(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Provided data is not a list")
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")

def get_last_item(data_list):
    validate_list(data_list)
    return data_list[-1]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20]
    try:
        print(get_last_item(sample_list))
    except Exception as e:
        print(e)

    empty_list = []
    try:
        print(get_last_item(empty_list))
    except Exception as e:
        print(e)