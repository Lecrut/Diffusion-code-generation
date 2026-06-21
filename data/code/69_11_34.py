class ElementAccessor:
    def __init__(self, sample_list):
        self.sample_list = sample_list

    def get_first(self):
        return self.sample_list[0]

    def get_second(self):
        return self.sample_list[1]

    def get_last(self):
        return self.sample_list[-1]

    def get_second_last(self):
        return self.sample_list[-2]

    def get_third_last(self):
        return self.sample_list[-3]

    def get_fourth_last(self):
        return self.sample_list[-4]

def access_elements(sample_list):
    accessor = ElementAccessor(sample_list)
    return {
        'first': accessor.get_first(),
        'second': accessor.get_second(),
        'last': accessor.get_last(),
        'second_last': accessor.get_second_last(),
        'third_last': accessor.get_third_last(),
        'fourth_last': accessor.get_fourth_last()
    }

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 600, 700]
    result = access_elements(sample_data)
    print(result)