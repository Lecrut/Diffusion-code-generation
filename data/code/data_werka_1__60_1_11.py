def get_last_item(data):
    try:
        return data[-1]
    except IndexError as e:
        raise ValueError("The provided list is empty") from e

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        last_element = get_last_item(sample_list)
        print(f"The last element of the list is: {last_element}")
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        get_last_item(empty_list)
    except ValueError as e:
        print(e)