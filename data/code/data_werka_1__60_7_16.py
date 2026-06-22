def get_last_element(lst):
    return lst[-1]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    EMPTY_LIST = []

    try:
        last_element = get_last_element(SAMPLE_LIST)
        print(f"Last element of SAMPLE_LIST: {last_element}")
    except IndexError as e:
        print(f"Error accessing last element of SAMPLE_LIST: {e}")

    try:
        last_element_empty = get_last_element(EMPTY_LIST)
        print(f"Last element of EMPTY_LIST: {last_element_empty}")
    except IndexError as e:
        print(f"Error accessing last element of EMPTY_LIST: {e}")