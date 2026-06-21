def access_elements(sample_list):
    first_element = sample_list[0]
    second_element = sample_list[1]
    last_element = sample_list[-1]
    second_last_element = sample_list[-2]
    middle_elements = sample_list[2:4]
    return {'first': first_element, 'second': second_element, 'last': last_element, 'second_last': second_last_element, 'middle': middle_elements}
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = access_elements(sample_data)
    print(result)