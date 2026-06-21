class ElementAccessor:
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

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65]
    accessor = ElementAccessor(sample_data)
    
    print("First element:", accessor.get_first_element())
    print("Second element:", accessor.get_second_element())
    print("Last element:", accessor.get_last_element())
    print("Second last element:", accessor.get_second_last_element())
    print("Third last element:", accessor.get_third_last_element())
    print("Fourth last element:", accessor.get_fourth_last_element())