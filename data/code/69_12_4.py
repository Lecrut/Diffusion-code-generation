def access_elements():
    sample_list = [10, 20, 30, 40, 50]
    positive_index = 2
    negative_index = -1

    element_positive = sample_list[positive_index]
    element_negative = sample_list[negative_index]

    return element_positive, element_negative

if __name__ == '__main__':
    result = access_elements()
    print(result)