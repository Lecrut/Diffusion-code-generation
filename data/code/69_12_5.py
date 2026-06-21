def access_elements(sample_list):
    first_element = sample_list[0]
    second_element = sample_list[1]
    last_element = sample_list[-1]
    second_last_element = sample_list[-2]
    middle_elements = sample_list[1:-1]
    return {'first_element': first_element, 'second_element': second_element, 'last_element': last_element, 'second_last_element': second_last_element, 'middle_elements': middle_elements}
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = access_elements(sample_data)
    print(result)