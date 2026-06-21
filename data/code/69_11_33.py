class ElementAccess:
    def __init__(self, sample_list):
        if not isinstance(sample_list, list) or len(sample_list) < 4:
            raise ValueError("Input must be a list with at least 4 elements.")
        self.sample_list = sample_list

    def get_element(self, index):
        return self.sample_list[index]

    def access_elements(self):
        return {
            'first': self.get_element(0),
            'second': self.get_element(1),
            'last': self.get_element(-1),
            'second_last': self.get_element(-2),
            'third_last': self.get_element(-3),
            'fourth_last': self.get_element(-4)
        }

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    accessor = ElementAccess(sample_data)
    result = accessor.access_elements()
    print(result)