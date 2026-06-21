def access_elements(lst):
    first_element = lst[0]
    second_element = lst[1]
    last_element = lst[-1]
    second_last_element = lst[-2]
    third_last_element = lst[-3]
    return {'first': first_element, 'second': second_element, 'last': last_element, 'second_last': second_last_element, 'third_last': third_last_element}
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = access_elements(sample_list)
    print(result)