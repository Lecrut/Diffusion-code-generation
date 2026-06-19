class ElementAccessor:
    EMPTY_LIST_ERROR_MESSAGE = "The list is empty"

    @staticmethod
    def get_first_element(elements):
        if not elements:
            raise IndexError(ElementAccessor.EMPTY_LIST_ERROR_MESSAGE)
        return elements[0]

if __name__ == '__main__':
    sample_list1 = [5, 15, 25, 35]
    sample_list2 = ['x', 'y', 'z']
    empty_sample_list = []

    try:
        print(ElementAccessor.get_first_element(sample_list1))
    except IndexError as e:
        print(e)

    try:
        print(ElementAccessor.get_first_element(sample_list2))
    except IndexError as e:
        print(e)

    try:
        print(ElementAccessor.get_first_element(empty_sample_list))
    except IndexError as e:
        print(e)