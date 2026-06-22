def find_first_element(data):
    try:
        if not data:
            raise ValueError("The list is empty.")
        return data[0]
    except IndexError as e:
        print(f"IndexError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    first_value = find_first_element(sample_list)
    if first_value is not None:
        print(first_value)