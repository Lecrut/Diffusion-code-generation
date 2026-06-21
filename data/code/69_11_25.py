class ElementAccessor:
    INDEX_FIRST = 0
    INDEX_SECOND = 1
    INDEX_LAST = -1
    INDEX_SECOND_LAST = -2
    INDEX_THIRD_LAST = -3
    INDEX_FOURTH_LAST = -4

    def __init__(self, sample_list):
        self.sample_list = sample_list

    @staticmethod
    def get_element_by_index(sample_list, index):
        return sample_list[index]

    def access_elements(self):
        first_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_FIRST)
        second_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_SECOND)
        last_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_LAST)
        second_last_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_SECOND_LAST)
        third_last_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_THIRD_LAST)
        fourth_last_element = ElementAccessor.get_element_by_index(self.sample_list, ElementAccessor.INDEX_FOURTH_LAST)

        return {
            'first': first_element,
            'second': second_element,
            'last': last_element,
            'second_last': second_last_element,
            'third_last': third_last_element,
            'fourth_last': fourth_last_element
        }

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    accessor = ElementAccessor(sample_data)
    result = accessor.access_elements()
    print(result)