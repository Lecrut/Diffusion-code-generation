MAX_INDEX = 10

def fetch_element(data_list, position):
    if not (0 <= position < len(data_list)):
        raise ValueError("Index out of bounds")
    return data_list[position]

if __name__ == '__main__':
    example_list = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]
    target_index = 5
    try:
        result = fetch_element(example_list, target_index)
        print(result)
    except ValueError as e:
        print(e)