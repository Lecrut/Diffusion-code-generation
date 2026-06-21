FILTER_ELEMENT = 2

def filter_element(input_list):
    return [item for item in input_list if item != FILTER_ELEMENT]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    filtered_list = filter_element(sample_list)
    print(filtered_list)