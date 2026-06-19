FIRST_ELEMENT_INDEX = 0

def fetch_first_element(int_list):
    return int_list[FIRST_ELEMENT_INDEX]

if __name__ == '__main__':
    test_data = [9, 18, 27, 36]
    result = fetch_first_element(test_data)
    print(result)