def fetch_last_element(array):
    if not array:
        return None
    return array[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print("Last element of sample_data:", fetch_last_element(sample_data))
    
    empty_data = []
    print("Last element of empty_data:", fetch_last_element(empty_data))
    
    single_element_data = [42]
    print("Last element of single_element_data:", fetch_last_element(single_element_data))