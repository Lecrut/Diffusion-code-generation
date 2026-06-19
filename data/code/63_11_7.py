def get_first_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [42, 7, 9]
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)