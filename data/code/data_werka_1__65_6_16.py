def get_element_at_index(data_list, index):
    try:
        element = data_list[index]
        assert 0 <= index < len(data_list), "Index out of bounds"
        return element
    except IndexError:
        return "Index out of bounds"

if __name__ == '__main__':
    SAMPLE_DATA = [5, 15, 25, 35, 45, 55, 65]
    TARGET_INDEX = 3

    result = get_element_at_index(SAMPLE_DATA, TARGET_INDEX)
    print(result)