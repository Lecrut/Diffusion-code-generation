LAST_ELEMENT_INDEX = -1

def fetch_last_element(sequence):
    return sequence[LAST_ELEMENT_INDEX]

if __name__ == '__main__':
    test_data = [99, 88, 77, 66, 55]
    print(fetch_last_element(test_data))