def access_list_elements():
    sample_list = [10, 20, 30, 40, 50]
    positive_index = 2
    negative_index = -3

    element_positive = sample_list[positive_index]
    element_negative = sample_list[negative_index]

    return element_positive, element_negative

if __name__ == '__main__':
    result = access_list_elements()
    print(result)