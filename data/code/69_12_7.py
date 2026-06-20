def access_list_elements():
    sample_list = [10, 20, 30, 40, 50]
    first_element = sample_list[0]
    third_element = sample_list[2]
    second_last_element = sample_list[-2]
    last_element = sample_list[-1]
    return (first_element, third_element, second_last_element, last_element)
if __name__ == '__main__':
    result = access_list_elements()
    print(result)