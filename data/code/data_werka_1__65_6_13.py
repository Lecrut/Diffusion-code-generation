def get_element_at_index(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_index = 7
    element = get_element_at_index(sample_data, target_index)
    print(element)