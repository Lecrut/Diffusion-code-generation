class DataAccessor:
    def __init__(self, sample_tuple, sample_dict):
        self.sample_tuple = sample_tuple
        self.sample_dict = sample_dict

    def get_last_element_of_tuple(self):
        return self.sample_tuple[-1]

    def get_second_to_last_value_of_dict(self):
        values_list = list(self.sample_dict.values())[0]
        return values_list[-2]

if __name__ == '__main__':
    sample_tuple = (5, 15, 25, 35, 45)
    sample_dict = {'x': [100, 200, 300], 'y': [400, 500, 600], 'z': [700, 800, 900]}
    
    accessor = DataAccessor(sample_tuple, sample_dict)
    
    last_element = accessor.get_last_element_of_tuple()
    second_to_last_value = accessor.get_second_to_last_value_of_dict()
    
    print(last_element)
    print(second_to_last_value)