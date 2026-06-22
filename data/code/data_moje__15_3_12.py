def _validate_list(data):
    length = len(data)
    if length < 2:
        raise ValueError("List must contain at least two elements")
    return length

def get_second_last_element(data):
    _validate_list(data)
    return data[-2]

if __name__ == '__main__':
    sample_integers = [3, 7, 19, 44, 88, 102]
    extracted = get_second_last_element(sample_integers)
    print(extracted)