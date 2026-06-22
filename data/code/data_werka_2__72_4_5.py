def get_elements_at_index(list_one, list_two, index):
    if index < 0 or index >= len(list_one) or index >= len(list_two):
        raise ValueError("Index out of range for one or both lists")
    element_one = list_one[index]
    element_two = list_two[index]
    return [(element_one, element_two)]

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = [40, 50, 60]
    target_index = 1
    output = get_elements_at_index(first_list, second_list, target_index)
    print(output)