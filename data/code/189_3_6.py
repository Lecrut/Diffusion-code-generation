class ListFilter:
    @staticmethod
    def remove_element(input_list, element_to_remove):
        return [item for item in input_list if item != element_to_remove]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    element_to_filter = 3
    filtered_list = ListFilter.remove_element(sample_list, element_to_filter)
    print(filtered_list)