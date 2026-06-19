def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        raise ValueError("The list is empty and has no first element.")

if __name__ == '__main__':
    sample_data = [5, 10, 15]
    print(get_first_element(sample_data))