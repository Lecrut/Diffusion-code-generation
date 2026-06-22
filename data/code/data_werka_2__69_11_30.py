def access_elements(sample_list):
    first_element = sample_list[0]
    second_element = sample_list[1]
    third_last_element = sample_list[-3]
    last_element = sample_list[-1]
    second_last_element = sample_list[-2]
    fourth_last_element = sample_list[-4]
    return {'first_element': first_element, 'second_element': second_element, 'third_last_element': third_last_element, 'last_element': last_element, 'second_last_element': second_last_element, 'fourth_last_element': fourth_last_element}
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    result = access_elements(sample_data)
    print(result)