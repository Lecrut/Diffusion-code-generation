MAX_EMPTY_LIST = "The list cannot be empty"

def get_largest_element(data):
    if not data:
        raise ValueError(MAX_EMPTY_LIST)
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 21]
    try:
        largest = get_largest_element(sample_list)
        print(largest)
    except ValueError as e:
        print(e)