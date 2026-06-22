class ListElementAccessor:
    def __init__(self, sample_list):
        self.sample_list = sample_list

    def get_first_element(self):
        return self.sample_list[0]

    def get_second_element(self):
        return self.sample_list[1]

    def get_last_element(self):
        return self.sample_list[-1]

    def get_second_last_element(self):
        return self.sample_list[-2]

    def get_third_last_element(self):
        return self.sample_list[-3]

    def get_fourth_last_element(self):
        return self.sample_list[-4]

    def access_elements(self):
        return {
            'first': self.get_first_element(),
            'second': self.get_second_element(),
            'last': self.get_last_element(),
            'second_last': self.get_second_last_element(),
            'third_last': self.get_third_last_element(),
            'fourth_last': self.get_fourth_last_element()
        }

if __name__ == '__main__':
    sample_data = [70, 80, 90, 100, 110, 120]
    accessor = ListElementAccessor(sample_data)
    result = accessor.access_elements()
    print(result)