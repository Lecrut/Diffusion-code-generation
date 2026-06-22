def get_first_element(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list.")
    return data[0]

if __name__ == '__main__':
    data = [5, 10, 15]
    try:
        print(get_first_element(data))
    except ValueError as e:
        print(e)