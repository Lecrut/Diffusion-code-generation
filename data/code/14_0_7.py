MIN_ITEMS = 3
THIRD_INDEX = 2

def get_third_element(data):
    if len(data) < MIN_ITEMS:
        raise IndexError("List has fewer than three items")
    return data[THIRD_INDEX]

if __name__ == '__main__':
    valid_data = ["alpha", "bravo", "charlie", "delta"]
    print(get_third_element(valid_data))
    invalid_data = ["alpha", "bravo"]
    try:
        print(get_third_element(invalid_data))
    except IndexError as err:
        print(err)