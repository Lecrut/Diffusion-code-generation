def access_list_elements(data_list):
    positive_index = 2
    negative_index = -1
    element_positive = data_list[positive_index]
    element_negative = data_list[negative_index]
    return element_positive, element_negative

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    result = access_list_elements(my_list)
    print(f"Element at positive index 2: {result[0]}")
    print(f"Element at negative index -1: {result[1]}")