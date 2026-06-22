class ElementAccessor:
    def __init__(self, sample_tuple, sample_dict):
        self.sample_tuple = sample_tuple
        self.sample_dict = sample_dict

    def validate_data(self):
        if not isinstance(self.sample_tuple, tuple) or len(self.sample_tuple) == 0:
            raise ValueError("Sample tuple is invalid")
        if not isinstance(self.sample_dict, dict) or len(self.sample_dict.values()) < 2:
            raise ValueError("Sample dictionary is invalid")

    def get_last_element_of_tuple(self):
        self.validate_data()
        return self.sample_tuple[-1]

    def get_second_to_last_value_of_dict(self):
        self.validate_data()
        second_key = list(self.sample_dict.keys())[1]
        values_list = self.sample_dict[second_key]
        if not isinstance(values_list, list) or len(values_list) < 2:
            raise ValueError("Values list in dictionary is invalid")
        return values_list[-2]

if __name__ == '__main__':
    sample_tuple = (5, 15, 25, 35, 45)
    sample_dict = {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]}
    
    accessor = ElementAccessor(sample_tuple, sample_dict)
    last_element = accessor.get_last_element_of_tuple()
    second_to_last_value = accessor.get_second_to_last_value_of_dict()
    
    print(last_element, second_to_last_value)