class Accessor:
    def __init__(self, data_tuple, data_dict):
        self.data_tuple = data_tuple
        self.data_dict = data_dict

    def get_last_element(self):
        return self.data_tuple[-1]

    def get_second_to_last_value(self):
        if len(self.data_dict) < 2:
            raise ValueError("Dictionary must have at least two values.")
        second_key = list(self.data_dict.keys())[1]
        return self.data_dict[second_key][-2]

if __name__ == '__main__':
    sample_tuple = (5, 15, 25, 35, 45)
    sample_dict = {'x': [10, 20, 30], 'y': [40, 50, 60], 'z': [70, 80, 90]}
    
    accessor = Accessor(sample_tuple, sample_dict)
    print(accessor.get_last_element())
    print(accessor.get_second_to_last_value())