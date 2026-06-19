class ListProcessor:
    SECOND_ELEMENT_INDEX = 1

    @staticmethod
    def get_second_element(lst):
        return lst[ListProcessor.SECOND_ELEMENT_INDEX]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    print(ListProcessor.get_second_element(my_list))