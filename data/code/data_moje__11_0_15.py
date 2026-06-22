def get_last_element(lst):
    return lst[-1]

LAST_INDEX = -1

def extract_tail(sequence):
    return sequence[0 if not sequence else LAST_INDEX]

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    result_value = get_last_element(test_data)
    print(result_value)