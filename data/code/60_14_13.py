def fetch_last_element(array):
    if not array:
        return None
    return array[-1]

if __name__ == '__main__':
    SAMPLE_ARRAY_1 = [1, 2, 3, 4, 5]
    SAMPLE_ARRAY_2 = ['a', 'b', 'c']
    SAMPLE_ARRAY_3 = []
    
    print("Last element of SAMPLE_ARRAY_1:", fetch_last_element(SAMPLE_ARRAY_1))
    print("Last element of SAMPLE_ARRAY_2:", fetch_last_element(SAMPLE_ARRAY_2))
    print("Last element of SAMPLE_ARRAY_3:", fetch_last_element(SAMPLE_ARRAY_3))