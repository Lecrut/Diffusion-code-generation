class DataAccessor:
    def __init__(self, tuple_data, dict_data):
        self.tuple_data = tuple_data
        self.dict_data = dict_data

    def get_last_element_tuple(self):
        return self.tuple_data[-1]

    def get_second_to_last_value_dict(self):
        values_list = list(self.dict_data.values())[1]
        return values_list[-2]

if __name__ == '__main__':
    sample_tuple = (5, 15, 25, 35, 45)
    sample_dict = {'x': [10, 20, 30], 'y': [40, 50, 60], 'z': [70, 80, 90]}

    accessor = DataAccessor(sample_tuple, sample_dict)
    last_element = accessor.get_last_element_tuple()
    second_to_last_value = accessor.get_second_to_last_value_dict()

    print("Last element of tuple:", last_element)
    print("Second-to-last value of dictionary's second key values list:", second_to_last_value)