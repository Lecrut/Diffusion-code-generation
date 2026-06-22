def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    if not data:
        raise ValueError("List is empty.")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))
    empty_list = []
    try:
        print(get_last_item(empty_list))
    except ValueError as e:
        print(f"Error: {e}")
    non_list = "not a list"
    try:
        print(get_last_item(non_list))
    except TypeError as e:
        print(f"Error: {e}")