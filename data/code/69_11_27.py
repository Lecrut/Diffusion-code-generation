def access_elements(sample_list):
    first_element = sample_list[0]
    second_element = sample_list[1]
    last_element = sample_list[-1]
    second_last_element = sample_list[-2]
    third_last_element = sample_list[-3]
    fourth_last_element = sample_list[-4]
    
    return {
        'first': first_element,
        'second': second_element,
        'last': last_element,
        'second_last': second_last_element,
        'third_last': third_last_element,
        'fourth_last': fourth_last_element
    }

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 600, 700]
    result = access_elements(sample_data)
    print(result)