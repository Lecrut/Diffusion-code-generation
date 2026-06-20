def access_list_elements():
    sample_data = [10, 20, 30, 40, 50]
    first_element = sample_data[0]
    third_element = sample_data[2]
    last_element = sample_data[-1]
    second_last_element = sample_data[-2]
    return (first_element, third_element, last_element, second_last_element)
if __name__ == '__main__':
    result = access_list_elements()
    print(result)