def find_last_element(data):
    try:
        if not data:
            raise ValueError("The list is empty")
        return data[-1]
    except TypeError:
        raise ValueError("Input must be a list")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        last_element = find_last_element(sample_list)
        print(last_element)
    except ValueError as e:
        print(e)