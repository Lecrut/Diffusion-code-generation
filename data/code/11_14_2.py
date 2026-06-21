def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise ValueError("List cannot be empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = get_last_item(sample_list)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)