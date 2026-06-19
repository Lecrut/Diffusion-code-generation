class Accessor:
    def __init__(self, data_tuple, data_dict):
        self.data_tuple = data_tuple
        self.data_dict = data_dict

    def get_last_element(self):
        if not isinstance(self.data_tuple, tuple) or len(self.data_tuple) == 0:
            raise ValueError("Data tuple is invalid")
        return self.data_tuple[-1]

    def get_second_to_last_value(self):
        if not isinstance(self.data_dict, dict) or len(self.data_dict.values()) < 2:
            raise ValueError("Data dictionary is invalid")
        values_list = next(iter(self.data_dict.values()))
        if not isinstance(values_list, list) or len(values_list) < 2:
            raise ValueError("Values list in dictionary is invalid")
        return values_list[-2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    accessor = Accessor(sample_tuple, sample_dict)
    last_element = accessor.get_last_element()
    second_to_last_value = accessor.get_second_to_last_value()
    print(last_element, second_to_last_value)