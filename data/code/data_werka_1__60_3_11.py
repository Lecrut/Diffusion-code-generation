ARRAY_INDEX_LAST = -1

def fetch_last_element(array):
    return array[ARRAY_INDEX_LAST]

if __name__ == '__main__':
    sample_data = [7, 8, 9, 10, 11]
    print(fetch_last_element(sample_data))