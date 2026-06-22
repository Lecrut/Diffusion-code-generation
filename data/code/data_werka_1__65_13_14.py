class ElementAccessor:
    SAMPLE_TUPLE = (10, 20, 30, 40, 50)
    SAMPLE_DICT = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

    @staticmethod
    def get_last_element_of_tuple():
        return ElementAccessor.SAMPLE_TUPLE[-1]

    @staticmethod
    def get_second_to_last_value_of_dict():
        values_list = list(ElementAccessor.SAMPLE_DICT.values())[1]
        return values_list[-2]

if __name__ == '__main__':
    last_element_tuple = ElementAccessor.get_last_element_of_tuple()
    second_to_last_value_dict = ElementAccessor.get_second_to_last_value_of_dict()
    print(last_element_tuple, second_to_last_value_dict)